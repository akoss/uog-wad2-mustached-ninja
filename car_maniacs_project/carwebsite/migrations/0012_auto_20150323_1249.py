# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0011_remove_model_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='acceleration',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='model',
            name='handling',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='model',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='model',
            name='security',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='model',
            name='speed',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
