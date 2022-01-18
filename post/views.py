from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

import pyupbit

def test():
    print('fwefwefw')

    # tickers = pyupbit.get_tickers(fiat="KRW")
    price = pyupbit.get_current_price("KRW-XRP")
    print(price)
    return
test()

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer