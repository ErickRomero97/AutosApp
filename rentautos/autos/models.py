# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Cliente(models.Model):
	identidad = models.CharField(max_length=15)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	email = models.EmailField()
	telefono = models.CharField(max_length=9)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)

@python_2_unicode_compatible
class Marca(models.Model):
	nombre = models.CharField(max_length=25)
	def __str__(self):
		return '{}'.format(self.nombre)

@python_2_unicode_compatible
class Modelo(models.Model):
	nombre = models.CharField(max_length=25)
	marca = models.ForeignKey(Marca)

	def __str__(self):
		return '{}'.format(self.nombre)

@python_2_unicode_compatible
class Auto(models.Model):
	auto = models.CharField(max_length=95)
	modelo = models.ForeignKey(Modelo)
	descripcion  = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	foto = models.ImageField(upload_to='photos', null=True, blank=True)
	disponible = models.BooleanField(default=True)
	
	def __str__(self):
		return '{} {}'.format(self.auto, self.foto)


class Factura(models.Model):
	cliente = models.ForeignKey(Cliente)
	auto = models.ForeignKey(Auto)
	dias = models.IntegerField()
	descuento = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
	fecha = models.DateField(auto_now_add=True)
	estado = models.BooleanField(default=True)

	
