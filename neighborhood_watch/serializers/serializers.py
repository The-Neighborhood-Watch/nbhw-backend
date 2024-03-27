from django.contrib.auth.models import User
from rest_framework import serializers
from entities.models import Entity


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email"]
