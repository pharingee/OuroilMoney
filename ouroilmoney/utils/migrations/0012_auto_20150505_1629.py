# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0011_partner_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ministry',
            options={'verbose_name': 'Ministry', 'verbose_name_plural': 'Ministries in Ghana'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'oil project', 'verbose_name_plural': 'Oil projects'},
        ),
        migrations.AlterField(
            model_name='ministry',
            name='ministry',
            field=models.CharField(max_length=500, null=True, verbose_name=b'ministry', blank=True),
        ),
    ]
