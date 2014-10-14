# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0002_auto_20141007_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetreportrevenue',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterUniqueTogether(
            name='annualbudgetreportrevenue',
            unique_together=set([('title', 'year')]),
        ),
    ]
