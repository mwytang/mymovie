# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=64)),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date commented')),
            ],
        ),
    ]
