# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0004_auto_20140930_0442'),
        ('reports', '0003_report'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reports',
        ),
    ]
