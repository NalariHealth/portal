# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20151019_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='relationship_to_subscriber',
            field=models.CharField(default='None', max_length=5, verbose_name=b'Relationship to Subscriber'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='subscriber_suffix',
            field=models.CharField(default='01', max_length=5, verbose_name=b'Subscriber Suffix'),
            preserve_default=False,
        ),
    ]
