# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_remove_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.TextField(),
        ),
    ]
