# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualbudgetproject',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='amount',
            field=models.DecimalField(verbose_name=b'total Amount', max_digits=19, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='project',
            field=models.ForeignKey(verbose_name=b'choose Project  From Other Reports', to='projects.AnnualBudgetProject'),
        ),
        migrations.AlterField(
            model_name='confirmsector',
            name='allocation',
            field=models.ForeignKey(verbose_name=b'choose Allocation From Other Report', to='allocations.ConfirmAllocation'),
        ),
        migrations.AlterField(
            model_name='confirmsector',
            name='annual_budget_sector',
            field=models.ForeignKey(verbose_name=b'choose Sector From Annual Budget Report', to='projects.AnnualBudgetSector'),
        ),
    ]
