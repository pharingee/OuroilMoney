# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0008_auto_20150123_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetreportrevenue',
            options={'ordering': ('-year',), 'get_latest_by': 'report', 'verbose_name': 'Revenue from Annual Budget Report', 'verbose_name_plural': 'Revenues from Annual Budget Report'},
        ),
    ]
