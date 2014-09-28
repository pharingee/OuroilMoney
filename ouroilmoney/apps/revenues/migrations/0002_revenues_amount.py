# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenues',
            name='amount',
            field=models.DecimalField(default=0, max_length=8, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
