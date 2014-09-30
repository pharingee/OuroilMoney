# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_delete_reports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='source',
            new_name='source_of_report',
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(max_length=4, verbose_name=b'date Issued'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(max_length=2, verbose_name=b'type of Report', choices=[(b'1Q', b'1st Quarter Report'), (b'2Q', b'2nd Quater Report'), (b'3Q', b'3rd Quater Report'), (b'4Q', b'4th Quarter Report'), (b'1YR', b'ANNUAL BUDGET REPORT'), (b'NONE OF THE ABOVE', b'None of the above')]),
        ),
        migrations.AlterField(
            model_name='report',
            name='source_url',
            field=models.URLField(help_text=b'Optional', max_length=500, null=True, verbose_name=b'url to Source', blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=500, verbose_name=b'title Of Report'),
        ),
    ]
