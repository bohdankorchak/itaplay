# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20160815_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_mac_address',
            new_name='mac_address',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player_status',
            new_name='status',
        ),
    ]