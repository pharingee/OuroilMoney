# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0008_auto_20150502_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministry',
            name='ministry',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name=b'ministry of Project', choices=[(b'WS', b'MINISTRY OF WORKS AND HOUSING'), (b'WA', b"MINISTY OF WOMEN & CHILDERN'S Affairs"), (b'TI', b'MINISITRY OF TRADE & INDUSTRY'), (b'TM', b'Ministry of Tourism & Modernization of The Capital City '), (b'RT', b'MINISTRY OF ROAD TRANSPORT'), (b'RC', b'MINISTY OF REGIONAL COOPERATION AND NEPAD (MRCN)'), (b'PD', b'MINISTRY OF PRIVATE SECTOR DEVELOPMENT & PSI'), (b'PA', b'MINISTRY OF PARLIAMENTARY AFFAIRS'), (b'YH', b'MINISTRY OF MANPOWER, YOUTH & EMPLOYMENT'), (b'LG', b'MINISTRY OF LOCAL GOVERNMENT AND RURAL DEVELOPMENT'), (b'ES', b'MINISTRY OF EDUCATION AND SPORTS'), (b'EG', b'MINISTRY OF ENERGY'), (b'ENS', b'MINISTRY OF ENVIRONMENT AND SCIENCE'), (b'CN', b'MINISTRY OF COMMUNICATON AND TECHNOLOGY'), (b'HT', b'MINISTRY OF HEALTH'), (b'IN', b'MINISTRY OF INFORMATION'), (b'JS', b"MINISTRY OF JUSTICE AND ATTORNEY GENERAL'S DEPARTMENT"), (b'LS', b'MINISTRY OF LANDS, AND FORESTRY & MINES')]),
        ),
    ]
