# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0004_model_averageratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=True,
        ),
    ]
