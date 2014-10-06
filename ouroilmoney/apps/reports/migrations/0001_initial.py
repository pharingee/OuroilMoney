# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualBudgetReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Report')),
                ('date', models.DateField(max_length=4, verbose_name=b'date Issued')),
                ('source_of_report', models.CharField(max_length=500, verbose_name=b'source Of Report')),
                ('source_url', models.URLField(help_text=b'Optional', max_length=500, null=True, verbose_name=b'url To Source', blank=True)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Annual Budget Report',
                'verbose_name_plural': 'Annual Budget Reports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfirmReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Report')),
                ('date', models.DateField(max_length=4, verbose_name=b'date Issued')),
                ('source_of_report', models.CharField(max_length=500, verbose_name=b'source Of Report')),
                ('source_url', models.URLField(help_text=b'Optional', max_length=500, null=True, verbose_name=b'url To Source', blank=True)),
                ('report_type', models.CharField(default=b'1Q', max_length=5, verbose_name=b'type Of Report', choices=[(b'1Q', b'1ST QUARTER REPORT'), (b'2Q', b'2ND QUARTER REPORT'), (b'3Q', b'3RD QUARTER REPORT'), (b'4Q', b'ANNUAL BUDGET REPORT'), (b'NFTA', b'NONE OF THE ABOVE')])),
                ('annual_budget_report', models.ForeignKey(to='reports.AnnualBudgetReport')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Confirm Report',
                'verbose_name_plural': 'Confirm Reports',
            },
            bases=(models.Model,),
        ),
    ]
