# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20140930_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_type',
            field=models.CharField(max_length=5, verbose_name=b'type Of Report', choices=[(b'ABR', b'ANNUAL BUDGET REPORT'), (b'1Q', b'1ST QUARTER REPORT'), (b'2Q', b'2ND QUARTER REPORT'), (b'3Q', b'3RD QUARTER REPORT'), (b'4Q', b'ANNUAL BUDGET REPORT'), (b'NFTA', b'NONE OF THE ABOVE')]),
        ),
    ]
