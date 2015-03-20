# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0007_model_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='picture',
            field=models.ImageField(default='', upload_to=b'', blank=True),
            preserve_default=False,
        ),
    ]
