# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crawl_data',
            fields=[
                ('requested_url', models.TextField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=250)),
                ('crawled_from_url', models.CharField(max_length=250)),
                ('depth_level', models.IntegerField()),
                ('created_at', models.DateField()),
                ('modified_at', models.DateField()),
            ],
            options={
                'db_table': 'app_crawl_data',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='crawl_data',
            unique_together=set([('image', 'crawled_from_url')]),
        ),
    ]