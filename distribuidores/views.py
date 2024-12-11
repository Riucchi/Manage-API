from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Distribuidores, Distribuidor
from .serializer import DistribuidoresSerializer, DistribuidorSerializer

class DistribuidoresListView(ListAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer
        

class DistribuidoresDeleteView(APIView):

    def delete(self, request, pk):
        try:
            distribuidor = Distribuidores.objects.get(pk=pk)
            distribuidor.delete()
            return Response({"Exito al eliminar": "Distribuidor eliminado"}, status=status.HTTP_200_OK)
        
        except Distribuidores.DoesNotExist:
            return Response({"Error": "Distribuidor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DistribuidoresPutView(APIView):

    def put(self, request, pk):
        try:
            distribuidor = Distribuidores.objects.get(pk=pk)
            serializer = DistribuidoresSerializer(distribuidor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Distribuidores.DoesNotExist:
            return Response({"Error": "Distribuidor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




class DistribuidoresPostView(CreateAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer



class DistribuidorListView(ListAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
    

class DistribuidorPostView(CreateAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer



class DistribuidorPutView(APIView):

    def put(self, request, pk):
        try:
            distribuidor = Distribuidor.objects.get(pk=pk)
            serializer = DistribuidorSerializer(distribuidor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Distribuidores.DoesNotExist:
            return Response({"Error": "Distribuidor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)