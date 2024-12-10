
from django.urls import path 
from .views import DistribuidoresListView, DistribuidoresPutView, DistribuidoresPostView, DistribuidorListView, DistribuidorPostView, DistribuidorPutView


urlpatterns = [
    path('lista/distribuidores', DistribuidoresListView.as_view(), name='lista-distribuidores'),
    path('editar-distribuidores/<int:pk>', DistribuidoresPutView.as_view(), name='editar-distribuidores'),
    path('crear-nuevos-distribuidores/',DistribuidoresPostView.as_view(), name='nuevo-distribuidores'),
    path('lista/distribuidor', DistribuidorListView.as_view(), name='lista-distribuidor'),
    path('crear-nuevo-distribuidor/', DistribuidorPostView.as_view(), name='nuevo-distribuidor'),
    path('editar-distriubidor/<int:pk>', DistribuidorPutView.as_view(), name='editar-distribuidor'),
]
