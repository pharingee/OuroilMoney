# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20141007_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmreport',
            name='report_type',
            field=models.CharField(default=b'1ST QUARTER REPORT', max_length=20, verbose_name=b'type Of Report', choices=[(b'1ST QUARTER REPORT', b'1ST QUARTER REPORT'), (b'2ND QUARTER REPORT', b'2ND QUARTER REPORT'), (b'3RD QUARTER REPORT', b'3RD QUARTER REPORT'), (b'4TH QUARTER REPORT', b'4TH QUARTER REPORT'), (b'MONITORING REPORT', b'MONITORING REPORT'), (b'NONE OF THE ABOVE', b'NONE OF THE ABOVE')]),
        ),
    ]
