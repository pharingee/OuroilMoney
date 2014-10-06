# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141006_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetproject',
            options={'ordering': ('-sector',), 'verbose_name': 'Annual Budget Report Project', 'verbose_name_plural': 'Annual Budget Reports Projects'},
        ),
        migrations.AlterModelOptions(
            name='annualbudgetsector',
            options={'ordering': ('-allocation',), 'verbose_name': 'Annual Budget Report Sector', 'verbose_name_plural': 'Annual Budget Reports Sectors'},
        ),
        migrations.AlterModelOptions(
            name='confirmproject',
            options={'ordering': ('-sector',), 'verbose_name': 'Project From Other Report', 'verbose_name_plural': 'Other Reports Projects'},
        ),
        migrations.AlterModelOptions(
            name='confirmsector',
            options={'ordering': ('-allocation',), 'verbose_name': 'Sector from Other Report', 'verbose_name_plural': 'Other Reports Sectors'},
        ),
        migrations.RemoveField(
            model_name='confirmproject',
            name='name',
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='project',
            field=models.ForeignKey(default=1, verbose_name=b'choose Project ', to='projects.AnnualBudgetProject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='confirmproject',
            name='sector',
            field=models.ForeignKey(verbose_name=b'choose Sector From Other Reports', to='projects.ConfirmSector'),
        ),
    ]
