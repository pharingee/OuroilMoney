# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20141005_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetreport',
            name='date',
            field=models.DateField(max_length=4, verbose_name=b'date Released'),
        ),
        migrations.AlterField(
            model_name='annualbudgetreport',
            name='summary',
            field=models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='confirmreport',
            name='date',
            field=models.DateField(max_length=4, verbose_name=b'date Released'),
        ),
        migrations.AlterField(
            model_name='confirmreport',
            name='summary',
            field=models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True),
        ),
    ]
