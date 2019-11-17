from django.contrib.auth.models import User

from .models import PileColor, HedgeHog, Comment
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class PileColorSerializer(serializers.ModelSerializer):
    """ A serializer for the PileColor model """
    class Meta:
        model = PileColor
        fields = ('id', 'name', 'description')


class HedgeHogSerializer(serializers.ModelSerializer):
    """ A serializer for the HedgeHog Model """
    class Meta:
        model = HedgeHog
        fields = ('id', 'name', 'image', 'pile_color', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for the Comment model """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'hedgehog', 'comment', 'visible', 'created')
