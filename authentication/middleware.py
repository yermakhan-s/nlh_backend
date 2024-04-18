from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.decorators import permission_classes
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from .serializers import UserSerializer
from .models import User


class AuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        auth = get_authorization_header(request).split()
        user = None
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            request.session['user_id'] = user.id

        # request.user = user

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
