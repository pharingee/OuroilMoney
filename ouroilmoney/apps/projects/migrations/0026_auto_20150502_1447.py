# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20150502_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetsector',
            name='allocation',
            field=models.ForeignKey(verbose_name=b'ABFA REPORT', to='allocations.AnnualBudgetAllocation'),
        ),
    ]
