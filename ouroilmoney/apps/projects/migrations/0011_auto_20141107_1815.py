# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20141107_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmsector',
            name='currency',
            field=models.CharField(default=b'GHS', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='confirmsector',
            name='amount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True),
        ),
    ]
