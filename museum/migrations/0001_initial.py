# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=90)),
                ('tag_1', models.CharField(max_length=90)),
                ('tag_2', models.CharField(max_length=90)),
                ('tag_3', models.CharField(max_length=90)),
                ('description', models.TextField()),
            ],
        ),
    ]
