# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0006_auto_20141123_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifting',
            name='partner',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Partner', blank=True),
            preserve_default=True,
        ),
    ]
