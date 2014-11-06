# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0002_lifting_lifting_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifting',
            name='lifting_receipt',
        ),
    ]
