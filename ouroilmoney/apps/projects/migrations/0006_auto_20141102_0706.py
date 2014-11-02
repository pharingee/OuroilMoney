# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20141030_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmsector',
            name='annual_budget_sector',
            field=models.ForeignKey(related_name=b'othersectors', verbose_name=b'choose Sector From Annual Budget Report', to='projects.AnnualBudgetSector'),
        ),
    ]
