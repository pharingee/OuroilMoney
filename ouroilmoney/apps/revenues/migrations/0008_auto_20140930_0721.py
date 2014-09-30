# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0007_auto_20140930_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenue',
            name='amount',
            field=models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money  '),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='report',
            field=models.ForeignKey(verbose_name=b'choose Report', to='reports.Report'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='title',
            field=models.CharField(max_length=500, verbose_name=b'title Of Revenue'),
        ),
    ]
