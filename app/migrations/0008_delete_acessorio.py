# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-05 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_locacao_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acessorio',
        ),
    ]