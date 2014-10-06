# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0003_auto_20141005_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmallocation',
            name='report',
            field=models.ForeignKey(verbose_name=b'Other Report in the same year', to='reports.ConfirmReport'),
        ),
    ]
