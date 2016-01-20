# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
