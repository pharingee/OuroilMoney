# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('projects', '0021_auto_20141216_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualbudgetproject',
            name='region',
        ),
        migrations.RemoveField(
            model_name='confirmproject',
            name='region',
        ),
        migrations.AddField(
            model_name='annualbudgetproject',
            name='regions',
            field=models.ManyToManyField(to='utils.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='regions',
            field=models.ManyToManyField(to='utils.Region'),
            preserve_default=True,
        ),
    ]
