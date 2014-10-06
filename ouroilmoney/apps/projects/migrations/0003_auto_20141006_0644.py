# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141006_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=3)),
                ('name', models.CharField(max_length=500, verbose_name=b'name of Project')),
                ('sector', models.ForeignKey(verbose_name=b'choose Sector From Annual Budget Reports', to='projects.AnnualBudgetSector')),
            ],
            options={
                'ordering': ('-sector',),
                'verbose_name': 'Project From Annual Budget Report',
                'verbose_name_plural': 'Projects from Annual Budget Reports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfirmProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=3)),
                ('name', models.CharField(max_length=500, verbose_name=b'name of Project')),
                ('sector', models.ForeignKey(verbose_name=b'choose Sector From Annual Budget Reports', to='projects.AnnualBudgetSector')),
            ],
            options={
                'ordering': ('-sector',),
                'verbose_name': 'Project From Annual Budget Report',
                'verbose_name_plural': 'Projects from Annual Budget Reports',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='confirmsector',
            name='allocation',
            field=models.ForeignKey(verbose_name=b'allocation from other report', to='allocations.ConfirmAllocation'),
        ),
    ]
