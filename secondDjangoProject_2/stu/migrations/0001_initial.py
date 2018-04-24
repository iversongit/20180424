# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_dex', models.BooleanField()),
                ('stu_birth', models.DateField(auto_now_add=True)),
                ('stu_operate_time', models.DateField(auto_now=True)),
                ('stu_tel', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'stu',
            },
        ),
    ]
