# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141014_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetsector',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
