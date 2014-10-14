# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141014_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmsector',
            old_name='total_amount',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='annualbudgetsector',
            name='total_amount',
        ),
    ]
