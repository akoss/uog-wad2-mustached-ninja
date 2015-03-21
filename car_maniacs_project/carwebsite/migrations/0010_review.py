# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carwebsite', '0009_auto_20150320_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed', models.IntegerField(default=0)),
                ('acceleration', models.IntegerField(default=0)),
                ('handling', models.IntegerField(default=0)),
                ('security', models.IntegerField(default=0)),
                ('model', models.ForeignKey(to='carwebsite.Model')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
