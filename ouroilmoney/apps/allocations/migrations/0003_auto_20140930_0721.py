# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0002_allocations_revenue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suballocations',
            name='allocation',
        ),
        migrations.DeleteModel(
            name='SubAllocations',
        ),
        migrations.RemoveField(
            model_name='allocations',
            name='revenue',
        ),
        migrations.AlterField(
            model_name='allocations',
            name='amount',
            field=models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money  '),
        ),
        migrations.AlterField(
            model_name='allocations',
            name='title',
            field=models.CharField(default=b'ABFA', help_text=b'For annual budget Funding Amount,please choose default(ABFA)', max_length=500, verbose_name=b'title Of Allocation'),
        ),
    ]
