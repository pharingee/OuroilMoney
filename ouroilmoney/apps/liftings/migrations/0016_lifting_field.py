# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0014_auto_20150505_1738'),
        ('liftings', '0015_remove_lifting_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifting',
            name='field',
            field=models.ForeignKey(related_name=b'liftings', default=None, to='utils.Field'),
            preserve_default=True,
        ),
    ]
