# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgehubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgehub',
            name='category',
            field=models.CharField(default='Government', max_length=14, choices=[(b'PIAC', b'PIAC'), (b'GOVERNMENT', b'GOVERNMENT'), (b'CIVIL SOCIETY', b'CIVIL SOCIETY')]),
            preserve_default=False,
        ),
    ]
