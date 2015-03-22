# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwebsite', '0010_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='url',
        ),
    ]
