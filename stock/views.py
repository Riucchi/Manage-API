from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializer import StockSerializer
# Create your views here.



class StockListView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockPostView(CreateAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDeleteView(DestroyAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockUpdateView(UpdateAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
