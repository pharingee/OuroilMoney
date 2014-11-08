# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20141107_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualbudgetproject',
            name='currency',
            field=models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
        ),
        migrations.AlterField(
            model_name='annualbudgetsector',
            name='currency',
            field=models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='currency',
            field=models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
        ),
        migrations.AlterField(
            model_name='confirmsector',
            name='currency',
            field=models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
        ),
    ]
