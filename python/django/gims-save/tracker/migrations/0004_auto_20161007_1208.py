# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-07 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160927_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderphenotypes',
            name='acc',
            field=models.CharField(default='HP:0000000', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderphenotypes',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='tracker.Orders'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.CharField(default=b'2016-10-07 12:08:32', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='updated',
            field=models.CharField(default=b'2016-10-07 12:08:32', max_length=50),
        ),
        migrations.AlterField(
            model_name='phenotypes',
            name='date',
            field=models.CharField(default=b'2016-10-07 12:08:32', max_length=200),
        ),
        migrations.AlterField(
            model_name='trackinglog',
            name='date',
            field=models.CharField(default=datetime.datetime(2016, 10, 7, 19, 8, 32, 207627, tzinfo=utc), max_length=50),
        ),
    ]
