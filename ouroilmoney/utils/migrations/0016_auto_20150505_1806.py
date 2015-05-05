# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0015_auto_20150505_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministry',
            name='ministry',
            field=models.CharField(max_length=500, unique=True, null=True, verbose_name=b'ministry', blank=True),
        ),
    ]
