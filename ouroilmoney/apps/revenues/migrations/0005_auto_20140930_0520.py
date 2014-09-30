# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0004_auto_20140930_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='amount',
            field=models.DecimalField(max_length=10, max_digits=10, decimal_places=2),
        ),
    ]
