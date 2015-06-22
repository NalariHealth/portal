# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150615_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='zoom_password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='zoom_username',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='zoom_password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='zoom_username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='zoom_id',
            field=models.CharField(default='blahblahblah', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='zoom_id',
            field=models.CharField(default='blahblahblah', max_length=70),
            preserve_default=False,
        ),
    ]
