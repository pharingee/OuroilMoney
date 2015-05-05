# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0010_auto_20150503_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('partner', models.CharField(max_length=b'500', verbose_name=b'oil partners')),
            ],
            options={
                'verbose_name': 'oil partner',
                'verbose_name_plural': 'Oil partners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('partner', models.CharField(max_length=b'500', verbose_name=b'oil project')),
            ],
            options={
                'verbose_name': 'oil project',
                'verbose_name_plural': 'Oil projects in ghana',
            },
            bases=(models.Model,),
        ),
    ]
