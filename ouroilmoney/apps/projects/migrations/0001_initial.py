# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=3)),
                ('name', models.CharField(max_length=500, verbose_name=b'name of Project')),
            ],
            options={
                'ordering': ('-sector',),
                'verbose_name': 'Annual Budget Report Project',
                'verbose_name_plural': 'Annual Budget Reports Projects',
            },
            bases=(models.Model,),
        ),
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
                'ordering': ('-allocation',),
                'verbose_name': 'Annual Budget Report Sector',
                'verbose_name_plural': 'Annual Budget Reports Sectors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfirmProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=3)),
                ('project', models.ForeignKey(verbose_name=b'choose Project ', to='projects.AnnualBudgetProject')),
            ],
            options={
                'ordering': ('-sector',),
                'verbose_name': 'Project From Other Report',
                'verbose_name_plural': 'Other Reports Projects',
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
                ('allocation', models.ForeignKey(verbose_name=b'allocation from other report', to='allocations.ConfirmAllocation')),
                ('annual_budget_sector', models.ForeignKey(verbose_name=b'sector from annual budget Report', to='projects.AnnualBudgetSector')),
            ],
            options={
                'ordering': ('-allocation',),
                'verbose_name': 'Sector from Other Report',
                'verbose_name_plural': 'Other Reports Sectors',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='sector',
            field=models.ForeignKey(verbose_name=b'choose Sector From Other Reports', to='projects.ConfirmSector'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annualbudgetproject',
            name='sector',
            field=models.ForeignKey(verbose_name=b'choose Sector From Annual Budget Reports', to='projects.AnnualBudgetSector'),
            preserve_default=True,
        ),
    ]
