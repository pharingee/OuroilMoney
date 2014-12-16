# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_annualbudgetsector_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetproject',
            name='town',
            field=models.CharField(max_length=100, null=True, verbose_name=b'town of Project', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='town',
            field=models.CharField(max_length=100, null=True, verbose_name=b'town of Project', blank=True),
            preserve_default=True,
        ),
    ]
