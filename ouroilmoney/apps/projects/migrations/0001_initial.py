# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0003_auto_20141005_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title of Sector')),
                ('total_amount', models.DecimalField(null=True, max_digits=19, decimal_places=3, blank=True)),
                ('allocation', models.ForeignKey(to='allocations.AnnualBudgetAllocation')),
            ],
            options={
                'ordering': ('allocation',),
                'verbose_name': 'Sector from Annual Budget Report',
                'verbose_name_plural': 'Sectors from Annual Budget Reports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfirmSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('total_amount', models.DecimalField(null=True, max_digits=19, decimal_places=3, blank=True)),
                ('allocation', models.ForeignKey(to='allocations.ConfirmAllocation')),
                ('annual_budget_sector', models.ForeignKey(verbose_name=b'sector from annual budget Report', to='projects.AnnualBudgetSector')),
            ],
            options={
                'ordering': ('allocation',),
                'verbose_name': 'Sector from Other Report',
                'verbose_name_plural': 'Sectors from Other Report',
            },
            bases=(models.Model,),
        ),
    ]
