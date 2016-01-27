# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default='cs', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(default=b'btech', max_length=20, choices=[(b'btech', b'B.Tech'), (b'mtech', b'M.Tech'), (b'mba', b'MBA & MAM'), (b'mca', b'MCA')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, serialize=False, primary_key=True),
        ),
    ]
