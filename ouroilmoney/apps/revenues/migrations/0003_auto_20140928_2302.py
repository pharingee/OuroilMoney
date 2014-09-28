# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0002_revenues_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenues',
            old_name='revenue',
            new_name='report',
        ),
    ]
