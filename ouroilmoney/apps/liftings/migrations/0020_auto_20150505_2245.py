# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0019_auto_20150505_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifting',
            name='field',
            field=models.ForeignKey(related_name=b'liftings', to='utils.Field'),
        ),
        migrations.AlterField(
            model_name='lifting',
            name='partner',
            field=models.ForeignKey(related_name=b'liftings', to='utils.Partner'),
        ),
    ]
