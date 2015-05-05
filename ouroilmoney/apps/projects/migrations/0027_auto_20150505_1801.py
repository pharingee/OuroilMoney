# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20150502_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmproject',
            name='ministry',
        ),
        migrations.AlterField(
            model_name='annualbudgetproject',
            name='ministry',
            field=models.ForeignKey(related_name=b'annualbudgetprojects', blank=True, to='utils.Ministry', null=True),
        ),
    ]
