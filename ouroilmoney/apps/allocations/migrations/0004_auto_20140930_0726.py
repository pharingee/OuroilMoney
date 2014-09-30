# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0003_auto_20140930_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'ABFA', help_text=b'For annual budget Funding Amount, please choose default(ABFA)', max_length=500, verbose_name=b'title Of Allocation')),
                ('amount', models.CommaSeparatedIntegerField(max_length=40, verbose_name=b'amount Of Money')),
                ('year', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Allocations',
        ),
    ]
