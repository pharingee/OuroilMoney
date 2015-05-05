# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0004_auto_20141107_1800'),
        ('projects', '0027_auto_20150505_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbaPriorityAreas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True)),
                ('currency', models.CharField(default=b'$', max_length=b'5', choices=[(b'GHS', b'GHS(GHANA CEDI)'), (b'$', b'$ (DOLLARS)')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'name f Priority Area')),
                ('abfa', models.ForeignKey(verbose_name=b'ABFA REPORT', to='allocations.AnnualBudgetAllocation')),
            ],
            options={
                'verbose_name': 'Abfa priority area ',
                'verbose_name_plural': 'Abfa priority areas',
            },
            bases=(models.Model,),
        ),
    ]
