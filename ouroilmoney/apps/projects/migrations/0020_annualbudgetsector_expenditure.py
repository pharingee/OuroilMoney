# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_remove_annualbudgetsector_sector_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetsector',
            name='expenditure',
            field=models.CharField(default=b'CAPITAL EXPENDITURE', max_length=500, verbose_name=b'Capital Expenditure or Recurrence Expenditure', choices=[(b'CAPITAL EXPENDITURE', b'CAPITAL EXPENDITURE'), (b'RECURRENCE EXPENDITURE', b'RECURRENCE EXPENDITURE')]),
            preserve_default=True,
        ),
    ]
