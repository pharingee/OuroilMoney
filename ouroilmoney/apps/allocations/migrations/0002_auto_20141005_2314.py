# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetallocation',
            options={'ordering': ('report',), 'verbose_name': 'Annual Budget Allocation', 'verbose_name_plural': 'Annual Budget Allocations'},
        ),
    ]
