# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_auto_20150218_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ministry', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'ministry of Project', choices=[(b'MINISTRY OF WORKS AND HOUSING', b'MINISTRY OF WORKS AND HOUSING'), (b"MINISTY OF WOMEN & CHILDERN'S Affairs", b"MINISTY OF WOMEN & CHILDERN'S Affairs"), (b'MINISITRY OF TRADE & INDUSTRY', b'MINISITRY OF TRADE & INDUSTRY'), (b'Ministry of Tourism & Modernization of The Capital City ', b'Ministry of Tourism & Modernization of The Capital City '), (b'MINISTRY OF ROAD TRANSPORT', b'MINISTRY OF ROAD TRANSPORT'), (b'MINISTY OF REGIONAL COOPERATION AND NEPAD (MRCN)', b'MINISTY OF REGIONAL COOPERATION AND NEPAD (MRCN)'), (b'MINISTRY OF PRIVATE SECTOR DEVELOPMENT & PSI', b'MINISTRY OF PRIVATE SECTOR DEVELOPMENT & PSI'), (b'MINISTRY OF PARLIAMENTARY AFFAIRS', b'MINISTRY OF PARLIAMENTARY AFFAIRS'), (b'MINISTRY OF MANPOWER, YOUTH & EMPLOYMENT', b'MINISTRY OF MANPOWER, YOUTH & EMPLOYMENT'), (b'MINISTRY OF LOCAL GOVERNMENT AND RURAL DEVELOPMENT', b'MINISTRY OF LOCAL GOVERNMENT AND RURAL DEVELOPMENT'), (b'MINISTRY OF EDUCATION AND SPORTS', b'MINISTRY OF EDUCATION AND SPORTS'), (b'MINISTRY OF ENERGY', b'MINISTRY OF ENERGY'), (b'MINISTRY OF ENVIRONMENT AND SCIENCE', b'MINISTRY OF ENVIRONMENT AND SCIENCE'), (b'MINISTRY OF COMMUNICATON AND TECHNOLOGY', b'MINISTRY OF COMMUNICATON AND TECHNOLOGY'), (b'MINISTRY OF HEALTH', b'MINISTRY OF HEALTH'), (b'MINISTRY OF INFORMATION', b'MINISTRY OF INFORMATION'), (b"MINISTRY OF JUSTICE AND ATTORNEY GENERAL'S DEPARTMENT", b"MINISTRY OF JUSTICE AND ATTORNEY GENERAL'S DEPARTMENT"), (b'MINISTRY OF LANDS, AND FORESTRY & MINES', b'MINISTRY OF LANDS, AND FORESTRY & MINES')])),
            ],
            options={
                'verbose_name': 'Ministry',
                'verbose_name_plural': 'Ministries',
            },
            bases=(models.Model,),
        ),
    ]
