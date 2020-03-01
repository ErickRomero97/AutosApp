from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from autos.models import Cliente, Marca, Modelo, Auto, Factura

class AutoSerializer(ModelSerializer):
	class Meta:
		model = Auto
		fields = ['id', 'auto', 'modelo', 'descripcion', 'precio', 'foto', 'disponible']

class AutoAddSerializer(ModelSerializer):
	class Meta:
		model = Auto
		fields = ['id', 'auto', 'modelo', 'descripcion', 'precio', 'foto', 'disponible']


class ClienteSerializer(ModelSerializer):
	class Meta:
		model = Cliente
		fields = ['id', 'identidad', 'nombre', 'apellido', 'email', 'telefono']

class ClienteAddSerializer(ModelSerializer):
	class Meta:
		model = Cliente
		fields = ['id', 'identidad' ,'nombre', 'apellido', 'email', 'telefono']



class FactutaSerializer(ModelSerializer):
	cliente = serializers.SlugRelatedField(read_only=True, slug_field='nombre')
	auto = AutoSerializer(read_only=True)
  	class Meta:
		model = Factura
		fields = ['id', 'cliente', 'auto', 'dias','descuento' ,'fecha', 'estado']

class FactutaAddSerializer(ModelSerializer):
  	class Meta:
		model = Factura
		fields = ['id', 'cliente', 'auto', 'dias', 'descuento', 'fecha', 'estado']