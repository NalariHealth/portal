# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20151019_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='name',
            field=models.CharField(unique=True, max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='ssn',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'Social Security Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='name',
            field=models.CharField(unique=True, max_length=35),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='username',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
