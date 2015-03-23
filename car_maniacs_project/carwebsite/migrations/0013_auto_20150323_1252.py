# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0012_auto_20150323_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='acceleration',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='handling',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='security',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='speed',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
