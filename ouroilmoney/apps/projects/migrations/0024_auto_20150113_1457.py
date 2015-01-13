# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20150113_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmproject',
            old_name='Video',
            new_name='video',
        ),
    ]
