# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0006_auto_20140930_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='amount',
            field=models.CommaSeparatedIntegerField(max_length=40),
        ),
    ]
