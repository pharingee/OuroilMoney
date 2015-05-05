# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgehubs', '0003_knowledgehub_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledgehub',
            old_name='subcategory',
            new_name='subcategorys',
        ),
    ]
