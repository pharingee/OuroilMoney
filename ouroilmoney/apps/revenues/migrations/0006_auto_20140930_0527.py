# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0005_auto_20140930_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='amount',
            field=models.DecimalField(max_digits=19, decimal_places=10),
        ),
    ]
