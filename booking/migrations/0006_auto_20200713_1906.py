# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-13 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_reservation_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
