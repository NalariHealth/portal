# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_source_id', models.CharField(max_length=50)),
                ('subscriber_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('dob', models.DateField()),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('secondary_phone', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('ssn', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pool_constrained', models.IntegerField(choices=[(1, b'True'), (2, b'False')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='practice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=35)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=50)),
                ('hours', models.CharField(max_length=50)),
                ('tax_id', models.CharField(max_length=50)),
                ('npi', models.CharField(max_length=50)),
                ('isolated', models.IntegerField(default=1, choices=[(1, b'True'), (2, b'False')])),
                ('feed', models.ForeignKey(to='feeds.feed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_id', models.CharField(max_length=50)),
                ('specialty_type', models.IntegerField()),
                ('prefix', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('dob', models.DateField()),
                ('identifier', models.CharField(max_length=50)),
                ('identifier_type', models.CharField(max_length=4, choices=[(b'SSN', b'SSN'), (b'EIN', b'EIN'), (b'UPIN', b'UPIN'), (b'NPI', b'NPI'), (b'DEA', b'DEA')])),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('feed', models.ForeignKey(to='feeds.feed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='provider_practice_rel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inactive', models.IntegerField(default=2, choices=[(1, b'True'), (2, b'False')])),
                ('practice_manager', models.IntegerField(default=1, choices=[(1, b'True'), (2, b'False')])),
                ('practice', models.ForeignKey(to='feeds.practice')),
                ('provider', models.ForeignKey(to='feeds.provider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='group_id',
            field=models.ForeignKey(to='feeds.practice'),
            preserve_default=True,
        ),
    ]
