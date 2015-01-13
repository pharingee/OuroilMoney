# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20141219_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annualbudgetproject',
            options={'ordering': ('-sector',), 'verbose_name': 'Annual Budget Project', 'verbose_name_plural': 'Annual Budget Projects'},
        ),
        migrations.AlterModelOptions(
            name='annualbudgetsector',
            options={'ordering': ('-allocation',), 'verbose_name': 'Annual Budget Sector', 'verbose_name_plural': 'Annual Budget Sectors'},
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='Video',
            field=models.FileField(upload_to=b'documents/video/%Y/%m/%d/', null=True, verbose_name=b'upload Videos', blank=True),
            preserve_default=True,
        ),
    ]
