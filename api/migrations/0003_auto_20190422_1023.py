# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-22 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190422_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceconfig',
            name='file_max_len',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='deviceconfig',
            name='record_end',
            field=models.IntegerField(),
        ),
    ]
