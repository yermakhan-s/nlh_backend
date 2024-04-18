import jwt
import datetime
from rest_framework import exceptions
from rest_framework.response import Response


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=30),
        'iat': datetime.datetime.now()
    }, 'access_secret', algorithm='HS256')


def decode_access_token(token):

    try:
        payload = jwt.decode(token, 'access_secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        raise exceptions.ParseError(
            'permission denied from decode')


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
        raise exceptions.NotAuthenticated('unauthenticated')
