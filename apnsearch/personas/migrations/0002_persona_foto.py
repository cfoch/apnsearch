# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.ImageField(default='profile.png', upload_to='fotos'),
            preserve_default=False,
        ),
    ]
