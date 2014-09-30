# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0004_auto_20140930_0442'),
        ('liftings', '0003_auto_20140930_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifting',
            name='revenue',
            field=models.ForeignKey(to='revenues.Revenue'),
            preserve_default=True,
        ),
    ]
