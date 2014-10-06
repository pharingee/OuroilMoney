# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0004_auto_20141006_0644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmallocation',
            options={'verbose_name': 'Allocation from Other Report', 'verbose_name_plural': 'Allocations from other Reports'},
        ),
    ]
