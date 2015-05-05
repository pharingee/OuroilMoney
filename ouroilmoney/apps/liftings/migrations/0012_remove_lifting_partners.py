# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0011_auto_20150505_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifting',
            name='partners',
        ),
    ]
