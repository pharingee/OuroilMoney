# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_annualbudgetsector_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmproject',
            name='amount',
            field=models.DecimalField(max_digits=19, decimal_places=3),
        ),
    ]
