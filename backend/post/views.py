from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

def test():
    print('fwefwefw')
    return
test()

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer