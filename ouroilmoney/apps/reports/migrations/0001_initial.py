# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('summary', models.TextField()),
                ('report_type', models.CharField(max_length=2, choices=[(b'1Q', b'1st Quarter'), (b'2Q', b'2nd Quater'), (b'3Q', b'3rd Quater'), (b'4Q', b'4th Quarter'), (b'YR', b'ANNUAL BUDGET REPORT'), (b'NONE OF THE ABOVE', b'None of the above')])),
                ('date', models.DateField(max_length=4)),
                ('source', models.CharField(max_length=500)),
                ('source_url', models.URLField(max_length=500)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
    ]
