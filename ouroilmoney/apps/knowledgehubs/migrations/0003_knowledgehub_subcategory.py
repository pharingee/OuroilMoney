# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgehubs', '0002_knowledgehub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgehub',
            name='subcategory',
            field=models.CharField(max_length=500, null=True, verbose_name=b'subcategory', blank=True),
            preserve_default=True,
        ),
    ]
