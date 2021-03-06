# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20160113_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_incorporacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
