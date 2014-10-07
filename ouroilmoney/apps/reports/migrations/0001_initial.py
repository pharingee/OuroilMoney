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
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Report')),
                ('date', models.DateField(max_length=4, verbose_name=b'date Released')),
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
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Report')),
                ('date', models.DateField(max_length=4, verbose_name=b'date Released')),
                ('source_of_report', models.CharField(max_length=500, verbose_name=b'source Of Report')),
                ('source_url', models.URLField(help_text=b'Optional', max_length=500, null=True, verbose_name=b'url To Source', blank=True)),
                ('report_type', models.CharField(default=b'1ST QUARTER REPORT', max_length=20, verbose_name=b'type Of Report', choices=[(b'1ST QUARTER REPORT', b'1ST QUARTER REPORT'), (b'2ND QUARTER REPORT', b'2ND QUARTER REPORT'), (b'3RD QUARTER REPORT', b'3RD QUARTER REPORT'), (b'4TH QUARTER REPORT', b'4TH QUARTER REPORT'), (b'NFTA', b'NONE OF THE ABOVE')])),
                ('annual_budget_report', models.ForeignKey(to='reports.AnnualBudgetReport')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Other Report',
                'verbose_name_plural': 'Other  Reports',
            },
            bases=(models.Model,),
        ),
    ]
