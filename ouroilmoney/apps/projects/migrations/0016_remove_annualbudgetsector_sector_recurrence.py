# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20141216_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualbudgetsector',
            name='sector_recurrence',
        ),
    ]
