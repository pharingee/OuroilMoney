# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20141106_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetproject',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annualbudgetsector',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annualbudgetproject',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='annualbudgetsector',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True),
        ),
    ]
