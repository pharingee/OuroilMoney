# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20141005_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetReportRevenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Revenue')),
                ('amount', models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money  ')),
                ('year', models.IntegerField(max_length=4)),
                ('report', models.ForeignKey(verbose_name=b'choose Annual Budget Report', to='reports.AnnualBudgetReport')),
            ],
            options={
                'ordering': ('-year',),
                'verbose_name': 'Revenue from Annual Budget Report',
                'verbose_name_plural': 'Revenues form Annual Budget Report',
            },
            bases=(models.Model,),
        ),
    ]
