# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetreportrevenue',
            name='report',
            field=models.ForeignKey(related_name=b'revenues', verbose_name=b'choose Annual Budget Report', to='reports.AnnualBudgetReport'),
        ),
    ]
