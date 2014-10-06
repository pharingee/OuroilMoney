# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0002_auto_20141005_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetreportrevenue',
            options={'ordering': ('-year',), 'verbose_name': 'Revenue from Annual Budget Report', 'verbose_name_plural': 'Revenues fm Annual Budget Report'},
        ),
    ]
