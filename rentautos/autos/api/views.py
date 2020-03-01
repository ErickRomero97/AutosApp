from autos.models import Auto, Cliente, Factura
from .serializers import (
  AutoSerializer,
  AutoAddSerializer,
  ClienteSerializer,
  ClienteAddSerializer,
  FactutaSerializer,
  FactutaAddSerializer
)
from rest_framework.generics import (
  ListAPIView,
  CreateAPIView,
  DestroyAPIView,
  UpdateAPIView,
  ListCreateAPIView,
  RetrieveAPIView,
)
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

class AutoTodo(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView,
                     mixins.UpdateModelMixin):
    """
     List all restaurant, or create a restaurant
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Auto.objects.all()
    serializer_class = AutoAddSerializer

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
      return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)






class AutoListAPIView(ListAPIView):
  queryset = Auto.objects.all()
  serializer_class = AutoSerializer

class AutoCreateAPIView(CreateAPIView):
  queryset = Auto.objects.all()
  serializer_class = AutoAddSerializer

class AutoUpdateAPIView(UpdateAPIView):
  queryset = Auto.objects.all()
  serializer_class = AutoAddSerializer

class AutoDetailAPIView(RetrieveAPIView):
  queryset = Auto.objects.all()
  serializer_class = AutoAddSerializer

class AutotDeleteAPIView(DestroyAPIView):
  queryset = Auto.objects.all()
  serializer_class = AutoAddSerializer





class ClienteListAPIView(ListAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer

class ClienteCreateAPIView(CreateAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteAddSerializer

class ClienteUpdateAPIView(UpdateAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteAddSerializer

class ClienteDeleteAPIView(DestroyAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteAddSerializer





class FacturaListAPIView(ListAPIView):
  queryset = Factura.objects.all()
  serializer_class = FactutaSerializer

class FacturaDetailAPIView(RetrieveAPIView):
  queryset = Factura.objects.all()
  serializer_class = FactutaAddSerializer

class FacturaCreateAPIView(CreateAPIView):
  queryset = Factura.objects.all()
  serializer_class = FactutaAddSerializer

class FacturaUpdateAPIView(UpdateAPIView):
  queryset = Factura.objects.all()
  serializer_class = FactutaAddSerializer

class FacturaDeleteAPIView(DestroyAPIView):
  queryset = Factura.objects.all()
  serializer_class = FactutaAddSerializer
