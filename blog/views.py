from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
# import generic views
from rest_framework.generics import ListCreateAPIView


class BlogAPI(ListCreateAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.all()
