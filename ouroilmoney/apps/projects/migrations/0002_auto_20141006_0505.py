# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmsector',
            options={'ordering': ('-allocation',), 'verbose_name': 'Sector from Other Report', 'verbose_name_plural': 'Sectors from Other Report'},
        ),
    ]
