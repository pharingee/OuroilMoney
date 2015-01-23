# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0007_auto_20150123_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualbudgetreportrevenue',
            name='money',
        ),
        migrations.AddField(
            model_name='annualbudgetreportrevenue',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
