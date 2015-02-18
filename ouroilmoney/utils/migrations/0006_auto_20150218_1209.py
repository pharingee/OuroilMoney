# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_auto_20150218_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsmessage',
            options={'verbose_name': 'Sms Message', 'verbose_name_plural': 'Sms Messages'},
        ),
    ]
