# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20160812_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adviseruser',
            old_name='company_id',
            new_name='id_company',
        ),
    ]
