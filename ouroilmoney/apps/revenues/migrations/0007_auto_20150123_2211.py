# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0006_auto_20150123_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualbudgetreportrevenue',
            old_name='amount',
            new_name='money',
        ),
    ]
