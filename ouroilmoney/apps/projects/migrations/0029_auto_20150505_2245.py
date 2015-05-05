# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_abapriorityareas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abapriorityareas',
            name='title',
            field=models.CharField(max_length=500, verbose_name=b'name  Priority Area'),
        ),
    ]
