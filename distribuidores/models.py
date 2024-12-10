from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from decimal import Decimal


class Distribuidor(models.Model):

    FACTURA_CHOICES = [
        ('1', 'A'),
        ('2', 'B'),
    ]

    tipo_de_factura = models.CharField(choices=FACTURA_CHOICES, max_length=20)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        tipo_de_factura_nombre = dict(self.FACTURA_CHOICES).get(self.tipo_de_factura, 'Desconocido')
        return f'{self.nombre}, Tipo de Factura: {tipo_de_factura_nombre}'


    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    distribuidor = models.ForeignKey(Distribuidor, null=True, default=None, on_delete=models.SET_NULL)
    precio_por_unidad = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.nombre


class Distribuidores(models.Model):
    distribuidor = models.ForeignKey(Distribuidor, null=True, default=None, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, default=None, on_delete=models.SET_NULL)
    cantidad_comprada = models.IntegerField(null=True)
    iva_discriminado = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    gasto_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.distribuidor.nombre}, {self.producto}, {self.gasto_total}"


@receiver(pre_save, sender=Distribuidores)
def calcular_iva_y_gasto_total(sender, instance, **kwargs):
    if instance.producto and instance.cantidad_comprada:
        precio_por_unidad = instance.producto.precio_por_unidad
        total_sin_iva = precio_por_unidad * Decimal(instance.cantidad_comprada)
        instance.iva_discriminado = total_sin_iva * Decimal('0.21')
        instance.gasto_total = total_sin_iva + instance.iva_discriminado