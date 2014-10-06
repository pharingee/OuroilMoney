# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetreportrevenue',
            name='year',
            field=models.IntegerField(default=2014, max_length=4),
        ),
    ]
