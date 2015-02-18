# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_auto_20150109_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=160)),
                ('user', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Unverified'), (b'2', b'Verified'), (b'3', b'Deleted')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name=b'publish')),
            ],
            options={
                'verbose_name': 'SMS Message',
                'verbose_name_plural': 'SMS Messages',
            },
            bases=(models.Model,),
        ),
    ]
