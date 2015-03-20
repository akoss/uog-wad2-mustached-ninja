# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0008_model_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='picture',
            field=models.ImageField(default='', upload_to=b'static/images', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='model',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', blank=True),
        ),
    ]
