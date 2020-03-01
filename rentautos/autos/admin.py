# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Auto)
admin.site.register(Factura)


