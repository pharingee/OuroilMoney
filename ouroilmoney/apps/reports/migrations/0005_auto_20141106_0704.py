# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20141105_0018'),
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
    ]
