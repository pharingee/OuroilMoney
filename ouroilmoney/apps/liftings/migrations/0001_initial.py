# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lifting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name=b'publish')),
                ('summary', models.TextField(help_text=b'Please copy and past summary of Report here.\n Optional', null=True, blank=True)),
                ('date', models.DateField()),
                ('volume_of_lifting', models.IntegerField()),
                ('selling_price', models.DecimalField(max_digits=10, decimal_places=3)),
                ('lifting_proceed', models.DecimalField(max_digits=19, decimal_places=3)),
                ('report', models.ForeignKey(to='reports.ConfirmReport')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Lifting from Report',
                'verbose_name_plural': 'Liftings from Reports',
            },
            bases=(models.Model,),
        ),
    ]
