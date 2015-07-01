# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150630_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='gen_user',
            field=models.ForeignKey(to='accounts.gen_user', null=True),
            preserve_default=True,
        ),
    ]
