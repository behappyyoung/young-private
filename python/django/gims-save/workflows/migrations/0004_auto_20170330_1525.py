# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-30 22:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0003_auto_20170330_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labworkflows',
            name='created_date',
            field=models.CharField(default=b'2017-03-30 15:25:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='labworkflows',
            name='updated_date',
            field=models.CharField(default=b'2017-03-30 15:25:41', max_length=50),
        ),
        migrations.AlterField(
            model_name='workflows',
            name='order_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.OrderType'),
        ),
    ]