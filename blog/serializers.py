from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    body = serializers.CharField()
    date = serializers.DateTimeField(read_only=True)
    summary = serializers.CharField(max_length=100, read_only=True)
    slug = serializers.SlugField(max_length=100, read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'date', 'summary', 'user', 'slug', 'user_id')
        depth = 1
