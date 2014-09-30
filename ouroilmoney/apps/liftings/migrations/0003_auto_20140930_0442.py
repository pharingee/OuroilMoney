# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liftings', '0002_liftings_barrel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lifting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('volume', models.IntegerField()),
                ('barrel_price', models.IntegerField()),
                ('lifting_proceed', models.IntegerField()),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Lifting',
                'verbose_name_plural': 'Liftings',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='liftings',
            name='revenue',
        ),
        migrations.DeleteModel(
            name='Liftings',
        ),
    ]
