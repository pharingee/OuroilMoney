# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0012_auto_20150505_1629'),
        ('liftings', '0012_remove_lifting_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifting',
            name='partner',
            field=models.ForeignKey(to='utils.Partner',null=True,blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lifting',
            name='project',
            field=models.ForeignKey(to='utils.Project',null=True,blank=True),
            preserve_default=True,
        ),
    ]
