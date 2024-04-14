from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.decorators import permission_classes
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import UserSerializer
from .models import User
from django.utils.decorators import method_decorator
from .middleware import AuthMiddleware

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
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

        # access_token = create_access_token(user.id)
        # refresh_token = create_refresh_token(user.id)

        # response = Response()

        # response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)

        return Response({'user_id': user.id})


# @method_decorator(AuthMiddleware, name='dispatch')
class UserAPIView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(pk=request.data['user_id'])
        except:
            raise APIException('Unauthenticated')
        # auth = get_authorization_header(request).split()
        # if auth and len(auth) == 2:
        #     token = auth[1].decode('utf-8')
        #     id = decode_access_token(token)

        #     user = User.objects.filter(pk=id).first()
        
        
        return Response({'user': user.id})

        # raise AuthenticationFailed('unauthenticated')


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
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