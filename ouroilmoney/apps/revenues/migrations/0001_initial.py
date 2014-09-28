# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20140928_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('year', models.IntegerField(max_length=4)),
                ('revenue', models.ForeignKey(to='reports.Reports')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
