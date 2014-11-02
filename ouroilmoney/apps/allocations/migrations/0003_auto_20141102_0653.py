# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0002_auto_20141014_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmallocation',
            name='annual_budget_allocation',
            field=models.ForeignKey(related_name=b'otherallocations', to='allocations.AnnualBudgetAllocation'),
        ),
    ]
