# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20140928_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'title of report')),
                ('report_type', models.CharField(max_length=2, choices=[(b'1Q', b'1st Quarter Report'), (b'2Q', b'2nd Quater Report'), (b'3Q', b'3rd Quater Report'), (b'4Q', b'4th Quarter Report'), (b'1YR', b'ANNUAL BUDGET REPORT'), (b'NONE OF THE ABOVE', b'None of the above')])),
                ('date', models.DateField(max_length=4)),
                ('source', models.CharField(max_length=500)),
                ('source_url', models.URLField(max_length=500, null=True, blank=True)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
    ]
