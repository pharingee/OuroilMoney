# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0014_auto_20150505_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifting',
            name='project',
        ),
    ]
