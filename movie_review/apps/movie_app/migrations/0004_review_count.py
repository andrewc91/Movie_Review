# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_remove_review_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
