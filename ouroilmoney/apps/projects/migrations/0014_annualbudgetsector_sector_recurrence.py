# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20141215_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetsector',
            name='sector_recurrence',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Capital expenditure or Recurrent expenditure', choices=[(b'CAPITAL EXPENDITURE', b'CAPITAL EXPENDITURE'), (b'RECURRENCE EXPENDITURE', b'RECURRENCE EXPENDITURE')]),
            preserve_default=True,
        ),
    ]
