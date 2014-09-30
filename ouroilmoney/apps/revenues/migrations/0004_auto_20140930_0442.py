# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_report'),
        ('liftings', '0003_auto_20140930_0442'),
        ('revenues', '0003_auto_20140928_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(max_length=8, max_digits=10, decimal_places=2)),
                ('year', models.IntegerField(max_length=4)),
                ('report', models.ForeignKey(to='reports.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='revenues',
            name='report',
        ),
        migrations.DeleteModel(
            name='Revenues',
        ),
    ]
