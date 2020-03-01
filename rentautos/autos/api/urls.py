from django.conf.urls import url
from .views import (
  AutoListAPIView,
  AutoCreateAPIView,
  AutoUpdateAPIView,
  AutoDetailAPIView,
  AutotDeleteAPIView,
  AutoTodo,
  ClienteListAPIView,
  ClienteCreateAPIView,
  ClienteUpdateAPIView,
  ClienteDeleteAPIView,
  FacturaListAPIView,
  FacturaDetailAPIView,
  FacturaCreateAPIView,
  FacturaUpdateAPIView,
  FacturaDeleteAPIView
)

urlpatterns = [
  url(r'^autos/$', AutoListAPIView.as_view(), name='autos'),
  url(r'^auto/listo/$', AutoTodo.as_view(), name='auto'),
  url(r'^auto/(?P<pk>\d+)/editar/$', AutoTodo.as_view(), name='autos-editar'),
  url(r'^auto/(?P<pk>\d+)/detalle/$', AutoDetailAPIView.as_view(), name='autos-detalle'),
  url(r'^auto/(?P<pk>\d+)/delete/$', AutotDeleteAPIView.as_view(), name='autos-delete'),


  url(r'^clientes/$', ClienteListAPIView.as_view(), name='clientes'),
  url(r'^cliente/add/$', ClienteCreateAPIView.as_view(), name='clientes'),
  url(r'^cliente/(?P<pk>\d+)/editar/$', ClienteUpdateAPIView.as_view(), name='cliente-editar'),
  url(r'^cliente/(?P<pk>\d+)/delete/$', ClienteDeleteAPIView.as_view(), name='cliente-delete'),


  url(r'^facturas/$', FacturaListAPIView.as_view(), name='factura'),
  url(r'^factura/add/$', FacturaCreateAPIView.as_view(), name='factura'),
  url(r'^factura/(?P<pk>\d+)/detalle/$', FacturaDetailAPIView.as_view(), name='autos-detalle'),
  url(r'^factura/(?P<pk>\d+)/editar/$', FacturaUpdateAPIView.as_view(), name='factura-editar'),
  url(r'^factura/(?P<pk>\d+)/delete/$', FacturaDeleteAPIView.as_view(), name='factura-delete'),
]
