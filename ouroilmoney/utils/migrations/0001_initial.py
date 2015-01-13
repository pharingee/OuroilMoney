# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'region of Project', choices=[(b'GREATER ACCRA REGION', b'GREATER REGION'), (b'ASHANTI REGION', b'ASHANTI REGION'), (b'NORTHERN REGION', b'NORTHERN REGION'), (b'UPPER WEST REGION', b'UPPER WEST REGION'), (b'UPPER EAST REGION', b'UPPER EAST REGION'), (b'EASTERN REGION', b'EASTERN REGION'), (b'WESTERN REGION', b'WESTERN REGION'), (b'CENTRAL REGION', b'CENTRAL REGION'), (b'VOLTA REGION', b'VOLTA REGION'), (b'BRONG AHAFO REGION', b'BRONG AHAFO REGION')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
