# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
    ]
