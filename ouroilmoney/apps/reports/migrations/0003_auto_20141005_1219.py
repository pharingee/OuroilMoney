# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20141005_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetreport',
            name='summary',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmreport',
            name='summary',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annualbudgetreport',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'publish'),
        ),
        migrations.AlterField(
            model_name='confirmreport',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'publish'),
        ),
    ]
