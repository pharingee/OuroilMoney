# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0004_auto_20140930_0442'),
        ('allocations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocations',
            name='revenue',
            field=models.ForeignKey(to='revenues.Revenue'),
            preserve_default=True,
        ),
    ]
