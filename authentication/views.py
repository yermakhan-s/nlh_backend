import datetime
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.decorators import permission_classes
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

from authentication import exceptions
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import UserSerializer, UserViewSetSerializer
from .models import User
from django.utils.decorators import method_decorator
from .authentication import JWTAuthentication

from rest_framework.viewsets import ModelViewSet

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):

        user = User.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials!')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key='refreshToken',
                            value=refresh_token, expires=datetime.datetime.now() + datetime.timedelta(days=7), httponly=True)
        serializer = UserSerializer(user, context={'request': request})
    

        response.data = {
            'access_token': access_token,
            'user_data': serializer.data
            
        }

        return response


# @method_decorator(AuthMiddleware, name='dispatch')
class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user, context={'request': request}).data)


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        if not refresh_token:
            return HttpResponse('not refresh token', status=401)
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })


class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response


class UserViewSet(ModelViewSet):
    serializer_class = UserViewSetSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    # filterset_fields=['category_id', 'user_id']