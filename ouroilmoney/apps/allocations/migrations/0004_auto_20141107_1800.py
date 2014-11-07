# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0003_auto_20141102_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetallocation',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmallocation',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
    ]
