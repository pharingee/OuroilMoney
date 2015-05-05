# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0013_auto_20150505_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifting',
            name='partner',
            field=models.ForeignKey(related_name=b'liftings', null=True,blank=True, to='utils.Partner'),
        ),
        migrations.AlterField(
            model_name='lifting',
            name='project',
            field=models.ForeignKey(related_name=b'liftings',null=True,blank=True to='utils.Project'),
        ),
    ]
