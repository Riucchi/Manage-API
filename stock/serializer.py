from rest_framework import serializers
from .views import Stock



class StockSerializer(serializers.Serializer):

    class Meta:
        model = Stock
        fields = ["id","producto","cantidad", "stock"]