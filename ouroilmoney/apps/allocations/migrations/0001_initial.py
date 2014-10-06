# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20141005_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetAllocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'ABFA', help_text=b'for ABFA allocations just use default', max_length=500, verbose_name=b'title Of Allocation')),
                ('amount', models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money')),
                ('report', models.ForeignKey(to='reports.AnnualBudgetReport')),
            ],
            options={
                'verbose_name': 'Annual Budget Allocation',
                'verbose_name_plural': 'Annual Budget Allocations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfirmAllocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money')),
                ('annual_budget_allocation', models.ForeignKey(to='allocations.AnnualBudgetAllocation')),
                ('report', models.ForeignKey(to='reports.ConfirmReport')),
            ],
            options={
                'verbose_name': 'Allocation form Other Report',
                'verbose_name_plural': 'Allocations form other Report',
            },
            bases=(models.Model,),
        ),
    ]
