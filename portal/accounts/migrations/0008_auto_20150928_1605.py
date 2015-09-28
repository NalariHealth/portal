# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20150630_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picfile', models.FileField(upload_to=b'static/user_photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gen_user',
            name='picture',
            field=models.ForeignKey(to='accounts.picture', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_1',
            field=models.ForeignKey(related_name='list_option_1', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_2',
            field=models.ForeignKey(related_name='list_option_2', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_3',
            field=models.ForeignKey(related_name='list_option_3', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_4',
            field=models.ForeignKey(related_name='list_option_4', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_5',
            field=models.ForeignKey(related_name='list_option_5', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='list_option_6',
            field=models.ForeignKey(related_name='list_option_6', on_delete=django.db.models.deletion.SET_NULL, to='accounts.list_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_1',
            field=models.ForeignKey(related_name='tile_1', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_2',
            field=models.ForeignKey(related_name='tile_2', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_3',
            field=models.ForeignKey(related_name='tile_3', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_4',
            field=models.ForeignKey(related_name='tile_4', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_5',
            field=models.ForeignKey(related_name='tile_5', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='tile_6',
            field=models.ForeignKey(related_name='tile_6', on_delete=django.db.models.deletion.SET_NULL, to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
    ]
