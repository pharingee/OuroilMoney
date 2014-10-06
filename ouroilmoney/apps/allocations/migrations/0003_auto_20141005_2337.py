# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0002_auto_20141005_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetallocation',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 5), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annualbudgetallocation',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'publish'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annualbudgetallocation',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2014, 10, 5), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='annualbudgetallocation',
            name='summary',
            field=models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmallocation',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 5), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmallocation',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'publish'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmallocation',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2014, 10, 5), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmallocation',
            name='summary',
            field=models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True),
            preserve_default=True,
        ),
    ]
