# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='report_type',
            field=models.CharField(max_length=2, choices=[(b'1Q', b'1st Quarter Report'), (b'2Q', b'2nd Quater Report'), (b'3Q', b'3rd Quater Report'), (b'4Q', b'4th Quarter Report'), (b'YR', b'ANNUAL BUDGET REPORT'), (b'NONE OF THE ABOVE', b'None of the above')]),
        ),
        migrations.AlterField(
            model_name='reports',
            name='source_url',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]
