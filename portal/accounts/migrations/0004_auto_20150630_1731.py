# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20150615_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='c_p_rel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gen_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='list_option',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('a_interior', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('list_option_1', models.ForeignKey(related_name='list_option_1', to='accounts.list_option', null=True)),
                ('list_option_2', models.ForeignKey(related_name='list_option_2', to='accounts.list_option', null=True)),
                ('list_option_3', models.ForeignKey(related_name='list_option_3', to='accounts.list_option', null=True)),
                ('list_option_4', models.ForeignKey(related_name='list_option_4', to='accounts.list_option', null=True)),
                ('list_option_5', models.ForeignKey(related_name='list_option_5', to='accounts.list_option', null=True)),
                ('list_option_6', models.ForeignKey(related_name='list_option_6', to='accounts.list_option', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tile_option',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('a_interior', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_1',
            field=models.ForeignKey(related_name='tile_1', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_2',
            field=models.ForeignKey(related_name='tile_2', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_3',
            field=models.ForeignKey(related_name='tile_3', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_4',
            field=models.ForeignKey(related_name='tile_4', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_5',
            field=models.ForeignKey(related_name='tile_5', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='tile_6',
            field=models.ForeignKey(related_name='tile_6', to='accounts.tile_option', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gen_user',
            name='settings',
            field=models.ForeignKey(default=1, to='accounts.settings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gen_user',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='c_p_rel',
            name='caregiver',
            field=models.ForeignKey(to='accounts.Caregiver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='c_p_rel',
            name='patient',
            field=models.ForeignKey(to='accounts.Patient'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='zoom_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='zoom_id',
        ),
    ]
