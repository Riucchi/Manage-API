from rest_framework import serializers
from .models import Distribuidor, Producto, Distribuidores

class DistribuidorSerializer(serializers.ModelSerializer):
    tipo_de_factura_display = serializers.CharField(source='get_tipo_de_factura_display', read_only=True)
    tipo_de_factura = serializers.ChoiceField(choices=Distribuidor.FACTURA_CHOICES)

    class Meta:
        model = Distribuidor
        fields = ['id', 'nombre', 'tipo_de_factura', 'tipo_de_factura_display']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio_por_unidad']  

class DistribuidoresSerializer(serializers.ModelSerializer):
    distribuidor = DistribuidorSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Distribuidores
        fields = ["id",'distribuidor', 'producto', 'cantidad_comprada', 'iva_discriminado', 'gasto_total']

    def create(self, validated_data):
        distribuidor_data = validated_data.pop('distribuidor')
        producto_data = validated_data.pop('producto')

        
        distribuidor_instance, created = Distribuidor.objects.get_or_create(
            nombre=distribuidor_data['nombre'],
            defaults=distribuidor_data  
        )

        
        producto_instance, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            defaults=producto_data 
        )

        
        distribuidor_instance = Distribuidores.objects.create(
            distribuidor=distribuidor_instance,
            producto=producto_instance,
            **validated_data
        )
        return distribuidor_instance
    


