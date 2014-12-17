# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_calenderofreport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CalenderOfReport',
            new_name='CalendarOfReport',
        ),
    ]
