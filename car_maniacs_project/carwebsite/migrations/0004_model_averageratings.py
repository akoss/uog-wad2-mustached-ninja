# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0003_auto_20150318_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='averageRatings',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
