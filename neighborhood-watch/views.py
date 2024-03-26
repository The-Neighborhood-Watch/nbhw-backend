from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

import logging

logger = logging.getLogger(__name__)


@api_view(["POST"])
def login(request):
    return Response({"message": "You are logged in."})


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        token = Token.objects.create(user=user)

        return Response(
            {"token": token.key, "user": UserSerializer(user).data},
            # {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def test_token(request):
    return Response({"message": "You are logged in."})
