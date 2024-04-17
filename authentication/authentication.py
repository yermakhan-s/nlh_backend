import jwt
import datetime
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(days=30),
        'iat': datetime.datetime.now()
    }, 'access_secret', algorithm='HS256')


def decode_access_token(token):

    try:
        payload = jwt.decode(token, 'access_secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')


def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(days=7),
        'iat': datetime.datetime.now()
    }, 'refresh_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms=['HS256'])
        print(payload)
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
