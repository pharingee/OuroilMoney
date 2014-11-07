# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0003_remove_lifting_lifting_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifting',
            name='lifting_receipt',
            field=models.FileField(upload_to=b'liftings/%Y/%m/%d', null=True, verbose_name=b'upload Lifting Receipts', blank=True),
            preserve_default=True,
        ),
    ]
