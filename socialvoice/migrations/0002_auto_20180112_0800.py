# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 08:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialvoice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='Name',
            new_name='name',
        ),
    ]
