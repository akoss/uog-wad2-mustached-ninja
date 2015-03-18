# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0002_auto_20150317_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='yearOfRelease',
        ),
        migrations.AddField(
            model_name='model',
            name='dateOfRelease',
            field=models.DateField(default=datetime.date(2015, 3, 18)),
            preserve_default=False,
        ),
    ]
