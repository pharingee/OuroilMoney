# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0008_auto_20150502_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifting',
            name='partner',
            field=models.CharField(default=b'JUBILEE', max_length=500, null=True, verbose_name=b'Partner', blank=True),
        ),
    ]
