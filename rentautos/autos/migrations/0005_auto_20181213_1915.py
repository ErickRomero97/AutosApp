# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-14 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_factura_descueto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='auto',
            field=models.CharField(max_length=95),
        ),
    ]
