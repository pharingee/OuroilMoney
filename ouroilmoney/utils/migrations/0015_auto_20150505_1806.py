# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0014_auto_20150505_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field',
            field=models.CharField(unique=True, max_length=b'500', verbose_name=b'oil field'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner',
            field=models.CharField(unique=True, max_length=b'500', verbose_name=b'oil partners'),
        ),
    ]
