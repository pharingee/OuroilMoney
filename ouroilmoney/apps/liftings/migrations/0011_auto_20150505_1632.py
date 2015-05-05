# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0010_auto_20150502_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lifting',
            old_name='partner',
            new_name='partners',
        ),
    ]
