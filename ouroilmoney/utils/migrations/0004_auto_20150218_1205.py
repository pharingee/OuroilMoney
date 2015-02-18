# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_smsmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsmessage',
            name='status',
            field=models.CharField(default=b'unverified', max_length=1, choices=[(b'unverified', b'Unverified'), (b'verified', b'Verified'), (b'deleted', b'Deleted')]),
        ),
    ]
