# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0009_auto_20150502_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifting',
            name='partner',
            field=models.CharField(default=b'JUBILEE', choices=[(b'GJ', b'GHANA JUBILEE'), (b'TN', b'TEN')], max_length=500, blank=True, null=True, verbose_name=b'Partner'),
        ),
    ]
