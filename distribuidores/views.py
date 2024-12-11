from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Distribuidores, Distribuidor
from .serializer import DistribuidoresSerializer, DistribuidorSerializer


class DistribuidoresListView(ListAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer
        


class DistribuidoresDeleteView(DestroyAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer


class DistribuidoresPutView(UpdateAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer


class DistribuidoresPostView(CreateAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer



class DistribuidorListView(ListAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
    

class DistribuidorPostView(CreateAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer



class DistribuidorPutView(UpdateAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer


class DistribuidorDeleteView(DestroyAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
