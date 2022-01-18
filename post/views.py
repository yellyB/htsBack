from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

import datetime
import pandas as pd
from pyupbit.request_api import _call_public_api
import requests

import pyupbit

# def test():
    # tickers = pyupbit.get_tickers(fiat="KRW")
    # price = pyupbit.get_current_price("KRW-XRP")
    # print(price)
    # df = get_ohlcv("KRW-BTC", interval="minute1", count=20)
    # print(df)
#     return
# test()


def get_ohlcv(ticker="KRW-BTC", interval="day", count=200, to=None):
    try:
        url = "https://api.upbit.com/v1/candles/minutes/5"

        if to == None:
            to = datetime.datetime.now()
        elif isinstance(to, str):
            to = pd.to_datetime(to).to_pydatetime()
        elif isinstance(to, pd._libs.tslibs.timestamps.Timestamp):
            to = to.to_pydatetime()

        if to.tzinfo is None:
            to = to.astimezone()
        to = to.astimezone(datetime.timezone.utc)
        to = to.strftime("%Y-%m-%d %H:%M:%S")

        contents = _call_public_api(url, market=ticker, count=count, to=to)[0]
        dt_list = [datetime.datetime.strptime(x['candle_date_time_kst'], "%Y-%m-%dT%H:%M:%S") for x in contents]
        # print(contents)
        df = pd.DataFrame(contents, columns=['opening_price', 'high_price', 'low_price', 'trade_price',
                                             'candle_acc_trade_volume'],
                          index=dt_list)
        df = df.rename(
            columns={"opening_price": "open", "high_price": "high", "low_price": "low", "trade_price": "close",
                     "candle_acc_trade_volume": "volume"})
        return df.sort_index()
    except Exception as x:
        print(x.__class__.__name__)
        return None

df = get_ohlcv("KRW-BTC", interval="minute1")
print(df)


class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer