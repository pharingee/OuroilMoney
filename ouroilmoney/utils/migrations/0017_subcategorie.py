# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0016_auto_20150505_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('subcategories', models.CharField(unique=True, max_length=b'500', verbose_name=b'subcategories for KnowledgeHub')),
            ],
            options={
                'verbose_name': 'subcategory for knowledge hub',
                'verbose_name_plural': 'subcategories for knowledge hub',
            },
            bases=(models.Model,),
        ),
    ]
