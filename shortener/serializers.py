from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Shortener

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class ShortenerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model =  Shortener
        fields = ('website', 'short_code', 'author', )


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['website', 'short_code',]