# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20141106_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmproject',
            name='remarks',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'FAILED', b'FAILED'), (b'ONGOING', b'ONGOING'), (b'FULFILLED', b'FULFILLED')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='annualbudgetproject',
            name='region',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'region of Project', choices=[(b'GREATER REGION', b'GREATER REGION'), (b'ASHANTI REGION', b'ASHANTI REGION'), (b'NORTHERN REGION', b'NORTHERN REGION'), (b'UPPER WEST REGION', b'UPPER WEST REGION'), (b'UPPER EAST REGION', b'UPPER EAST REGION'), (b'EASTERN REGION', b'EASTERN REGION'), (b'WESTERN REGION', b'WESTERN REGION'), (b'CENTRAL REGION', b'CENTRAL REGION'), (b'VOLTA REGION', b'VOLTA REGION'), (b'BRONG AHAFO REGION', b'BRONG AHAFO REGION')]),
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='region',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'region of Project', choices=[(b'GREATER REGION', b'GREATER REGION'), (b'ASHANTI REGION', b'ASHANTI REGION'), (b'NORTHERN REGION', b'NORTHERN REGION'), (b'UPPER WEST REGION', b'UPPER WEST REGION'), (b'UPPER EAST REGION', b'UPPER EAST REGION'), (b'EASTERN REGION', b'EASTERN REGION'), (b'WESTERN REGION', b'WESTERN REGION'), (b'CENTRAL REGION', b'CENTRAL REGION'), (b'VOLTA REGION', b'VOLTA REGION'), (b'BRONG AHAFO REGION', b'BRONG AHAFO REGION')]),
        ),
    ]
