# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmreport',
            options={'ordering': ('-date',), 'verbose_name': 'other Report', 'verbose_name_plural': 'Other  Reports'},
        ),
        migrations.AddField(
            model_name='annualbudgetreport',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmreport',
            name='is_published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='confirmreport',
            name='report_type',
            field=models.CharField(default=b'1Q', max_length=5, verbose_name=b'type Of Report', choices=[(b'1Q', b'1ST QUARTER REPORT'), (b'2Q', b'2ND QUARTER REPORT'), (b'3Q', b'3RD QUARTER REPORT'), (b'4Q', b'4TH QUARTER REPORT'), (b'NFTA', b'NONE OF THE ABOVE')]),
        ),
    ]
