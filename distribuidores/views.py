from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Distribuidores, Distribuidor
from .serializer import DistribuidoresSerializer, DistribuidorSerializer

class DistribuidoresListView(ListAPIView):
    queryset = Distribuidores.objects.all()
    serializer_class = DistribuidoresSerializer
        


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




class DistribuidoresPostView(APIView):


    def post(self, request):
        try:
            serializer = DistribuidoresSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class DistribuidorListView(ListAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
    

class DistribuidorPostView(APIView):

    def post(self, request):
        try:
            serializer = DistribuidorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



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