# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20140930_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(max_length=5, verbose_name=b'type Of Report', choices=[(b'ABR', b'ANNUAL BUDGET REPORT'), (b'1Q', b'1ST QUARTER REPORT'), (b'2Q', b'2nd QUARTER REPORT'), (b'3Q', b'3rd QUARTER REPORT'), (b'4Q', b'4th QUARTER REPORT'), (b'NFTA', b'NONE OF THE ABOVE')]),
        ),
        migrations.AlterField(
            model_name='report',
            name='source_of_report',
            field=models.CharField(max_length=500, verbose_name=b'source Of Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='source_url',
            field=models.URLField(help_text=b'Optional', max_length=500, null=True, verbose_name=b'url To Source', blank=True),
        ),
    ]
