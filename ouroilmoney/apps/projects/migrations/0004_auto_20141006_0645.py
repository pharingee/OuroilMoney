# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141006_0644'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnnualBudgetProjects',
            new_name='AnnualBudgetProject',
        ),
        migrations.RenameModel(
            old_name='ConfirmProjects',
            new_name='ConfirmProject',
        ),
    ]
