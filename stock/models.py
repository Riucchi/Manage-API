from django.db import models

from distribuidores.models import Producto




class Stock(models.Model):
    producto = models.ForeignKey(Producto, null=True, default=None, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    stock = models.BooleanField(default=True)


    def __str__(self):
        return self.producto, self.cantidad