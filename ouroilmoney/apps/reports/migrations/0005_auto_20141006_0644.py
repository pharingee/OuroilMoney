# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20141005_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmreport',
            options={'ordering': ('-date',), 'verbose_name': 'Other Report', 'verbose_name_plural': 'Other  Reports'},
        ),
    ]
