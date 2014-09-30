# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(max_length=8, max_digits=10, decimal_places=2)),
                ('receipt', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubAllocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(max_length=8, max_digits=10, decimal_places=2)),
                ('allocation', models.ForeignKey(to='allocations.Allocations')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
