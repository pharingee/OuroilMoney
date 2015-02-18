# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20150123_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetreport',
            options={'ordering': ('-date',), 'verbose_name': 'Annual Budget Report', 'verbose_name_plural': 'Annual Budget Reports'},
        ),
    ]
