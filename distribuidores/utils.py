from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Distribuidor, Producto, Distribuidores
from openpyxl import Workbook
import os


"""
    Excel Processing

"""



@receiver(post_save, sender=Distribuidor)
@receiver(post_save, sender=Distribuidores)
@receiver(post_save, sender=Producto)
def export_to_excel(sender, instance, created, **kwargs):
    wb = Workbook()
    ws = wb.active  # Accede a la hoja activa de manera explícita
    ws.title = "Distribuidores-Distribuidor-Productos"

    if sender == Distribuidor:
        headers = ["ID", "Tipo de Factura", 'Nombre']
        data = [(instance.id, instance.tipo_de_factura, instance.nombre)]
    elif sender == Distribuidores:
        headers = ['ID', 'Nombre', 'Distribuidor', 'Precio por Unidad']
        # Accede al precio por unidad a través del producto relacionado
        precio_por_unidad = instance.producto.precio_por_unidad if instance.producto else None
        data = [(instance.id, instance.distribuidor.nombre if instance.distribuidor else None, precio_por_unidad)]
    elif sender == Producto:
        headers = ['ID', 'Distribuidor', 'Producto', 'Cantidad Comprada', 'IVA Discriminado', 'Gasto Total']
        data = [(instance.id, instance.distribuidor.nombre if instance.distribuidor else None, instance.nombre, instance.cantidad_comprada, instance.iva_discriminado, instance.gasto_total)]

    ws.append(headers)

    for row in data:
        ws.append(row)

    file_path = os.path.join('./excel', 'datos.xlsx')
    wb.save(file_path)