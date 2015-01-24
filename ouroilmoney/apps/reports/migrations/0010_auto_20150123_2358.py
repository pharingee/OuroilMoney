# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20141217_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetreport',
            options={'ordering': ('-date',), 'get_latest_by': 'date', 'verbose_name': 'Annual Budget Report', 'verbose_name_plural': 'Annual Budget Reports'},
        ),
    ]
