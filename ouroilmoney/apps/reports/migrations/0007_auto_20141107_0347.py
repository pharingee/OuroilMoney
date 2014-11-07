# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20141107_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualbudgetreport',
            name='docfile',
        ),
        migrations.RemoveField(
            model_name='confirmreport',
            name='docfile',
        ),
        migrations.AddField(
            model_name='annualbudgetreport',
            name='document',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d/', null=True, verbose_name=b'upload Docs and Publications', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmreport',
            name='document',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d/', null=True, verbose_name=b'upload Docs and Publications', blank=True),
            preserve_default=True,
        ),
    ]
