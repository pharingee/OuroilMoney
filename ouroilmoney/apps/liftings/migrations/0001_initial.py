# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liftings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('volume', models.IntegerField()),
                ('lifting_proceed', models.IntegerField()),
                ('revenue', models.ForeignKey(to='revenues.Revenues')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Lifting',
                'verbose_name_plural': 'Liftings',
            },
            bases=(models.Model,),
        ),
    ]
