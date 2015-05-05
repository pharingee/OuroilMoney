# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0018_auto_20150505_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='subcategories',
            new_name='subcategory',
        ),
    ]
