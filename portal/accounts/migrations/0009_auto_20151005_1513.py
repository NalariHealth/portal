# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150928_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picfile',
            field=models.FileField(upload_to=b'user_photos'),
            preserve_default=True,
        ),
    ]
