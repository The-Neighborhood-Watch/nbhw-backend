import logging

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

logger = logging.getLogger(__name__)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = get_object_or_404(User, username=username)
    if not user.check_password(password):
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND
        )
    token, created = Token.objects.get_or_create(user=user)

    return Response(
        {"token": token.key, "user": UserSerializer(user).data},
        status=status.HTTP_200_OK,
    )


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
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"message": "You are authenticated!"}, status=status.HTTP_200_OK)
