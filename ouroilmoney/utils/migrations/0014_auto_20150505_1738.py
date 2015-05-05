# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0015_remove_lifting_project'),
        ('utils', '0013_auto_20150505_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('field', models.CharField(max_length=b'500', verbose_name=b'oil field')),
            ],
            options={
                'verbose_name': 'oil field',
                'verbose_name_plural': 'Oil field',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
