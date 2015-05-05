# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgehubs', '0008_auto_20150505_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgehub',
            name='subcategory',
            field=models.ForeignKey(related_name=b'knowledgehubs', default=None, verbose_name=b'subcategory', to='utils.SubCategory'),
        ),
    ]
