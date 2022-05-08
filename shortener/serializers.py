from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Shortener

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class ShortenerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='shortener:redirect',
        lookup_field='short_code'
    )
    class Meta:
        model =  Shortener
        fields = ('short_code', 'url', 'website')


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['created_at', 'last_visited', 'visit_count']