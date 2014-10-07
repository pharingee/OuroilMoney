# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetReportRevenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Revenue')),
                ('amount', models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money  ')),
                ('year', models.IntegerField(default=2014, max_length=4)),
                ('report', models.ForeignKey(verbose_name=b'choose Annual Budget Report', to='reports.AnnualBudgetReport')),
            ],
            options={
                'ordering': ('-year',),
                'verbose_name': 'Revenue from Annual Budget Report',
                'verbose_name_plural': 'Revenues from Annual Budget Report',
            },
            bases=(models.Model,),
        ),
    ]
