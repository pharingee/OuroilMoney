# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20141106_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetreport',
            name='docfile',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d', null=True, verbose_name=b'upload Docs and Publications', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmreport',
            name='docfile',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d', null=True, verbose_name=b'upload Docs and Publications', blank=True),
            preserve_default=True,
        ),
    ]
