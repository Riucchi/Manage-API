from django.urls import path
from .views import StockListView, StockPostView, StockDeleteView, StockUpdateView

urlpatterns = [
    path('lista-stock', StockListView.as_view(), name="lista-stock"),
    path('crear-stock', StockPostView.as_view(), name="crear-stock"),
    path('editar-stock/<int:pk>', StockUpdateView.as_view(), name="editar-stock"),
    path('borrar-stock/<int:pk>', StockDeleteView.as_view(), name="borrar-stock"),
]
