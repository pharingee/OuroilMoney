# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20141108_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='confirmproject',
            options={'ordering': ('-sector',), 'verbose_name': 'Monitoring Report on Project', 'verbose_name_plural': 'Monitoring Reports on Projects'},
        ),
        migrations.AddField(
            model_name='confirmproject',
            name='image',
            field=models.ImageField(default=None, upload_to=b'documents/monitoringprojects/%Y/%m/%d/', null=True, verbose_name=b'Upload Image For Project', blank=True),
            preserve_default=True,
        ),
    ]
