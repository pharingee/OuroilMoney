# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0018_auto_20150505_1817'),
        ('knowledgehubs', '0004_auto_20150505_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgehub',
            name='SubCategory',
            field=models.ForeignKey(related_name=b'knowledgehubs', default=None, to='utils.SubCategory'),
            preserve_default=True,
        ),
    ]
