# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0005_auto_20141107_0347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lifting',
            options={'ordering': ('-date',), 'get_latest_by': 'date', 'verbose_name': 'Lifting from Report', 'verbose_name_plural': 'Liftings from Reports'},
        ),
    ]
