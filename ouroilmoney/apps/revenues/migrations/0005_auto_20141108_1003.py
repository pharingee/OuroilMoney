# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0004_annualbudgetreportrevenue_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetreportrevenue',
            name='currency',
            field=models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
        ),
    ]
