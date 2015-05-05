# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0018_auto_20150505_1817'),
        ('knowledgehubs', '0005_knowledgehub_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledgehub',
            name='SubCategory',
        ),
        migrations.RemoveField(
            model_name='knowledgehub',
            name='subcategorys',
        ),
        migrations.AddField(
            model_name='knowledgehub',
            name='subCategory',
            field=models.ForeignKey(related_name=b'knowledgehubs', default=None, verbose_name=b'subcategory', to='utils.SubCategory'),
            preserve_default=True,
        ),
    ]
