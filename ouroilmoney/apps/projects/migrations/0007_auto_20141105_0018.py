# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20141102_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmproject',
            name='project',
            field=models.ForeignKey(related_name=b'otherprojects', verbose_name=b'choose Project  From Other Reports', to='projects.AnnualBudgetProject'),
        ),
    ]
