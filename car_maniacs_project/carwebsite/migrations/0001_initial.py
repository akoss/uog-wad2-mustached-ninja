# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128)),
                ('url', models.URLField()),
                ('speed', models.IntegerField(default=0)),
                ('acceleration', models.IntegerField(default=0)),
                ('handling', models.IntegerField(default=0)),
                ('security', models.IntegerField(default=0)),
                ('dateOfRelease', models.DateField()),
                ('price', models.IntegerField(default=0)),
                ('manufacturer', models.ForeignKey(to='carwebsite.Manufacturer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
