# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgehubs', '0006_auto_20150505_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledgehub',
            old_name='subCategory',
            new_name='subcategory',
        ),
    ]
