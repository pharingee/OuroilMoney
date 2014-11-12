# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeHub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title Of Report')),
                ('date', models.DateField(max_length=4, verbose_name=b'date Released')),
                ('document', models.FileField(upload_to=b'documents/%Y/%m/%d/', verbose_name=b'upload Docs and Publications')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
