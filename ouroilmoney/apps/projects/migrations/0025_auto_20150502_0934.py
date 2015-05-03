# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0007_ministry'),
        ('projects', '0024_auto_20150113_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualbudgetproject',
            name='ministry',
            field=models.ForeignKey(blank=True, to='utils.Ministry', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='ministry',
            field=models.ForeignKey(blank=True, to='utils.Ministry', null=True),
            preserve_default=True,
        ),
    ]
