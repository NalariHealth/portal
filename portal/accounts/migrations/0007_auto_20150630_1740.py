# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150630_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregiver',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user'),
            preserve_default=True,
        ),
    ]
