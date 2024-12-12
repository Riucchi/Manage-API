from rest_framework import serializers
from .views import Stock
from distribuidores.serializer import ProductoSerializer



class StockSerializer(serializers.Serializer):
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Stock
        fields = ["id","producto","cantidad", "stock"]