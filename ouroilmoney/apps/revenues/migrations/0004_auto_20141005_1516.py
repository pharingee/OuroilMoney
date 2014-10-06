# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0003_auto_20141005_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetreportrevenue',
            options={'ordering': ('-year',), 'verbose_name': 'Revenue from Annual Budget Report', 'verbose_name_plural': 'Revenues from Annual Budget Report'},
        ),
    ]
