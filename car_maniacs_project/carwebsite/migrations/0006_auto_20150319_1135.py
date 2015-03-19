# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0005_manufacturer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
