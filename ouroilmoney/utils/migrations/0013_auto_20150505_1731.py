# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0012_auto_20150505_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='partner',
            new_name='project',
        ),
    ]
