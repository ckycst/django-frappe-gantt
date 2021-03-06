# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_model_to_dict.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20180323_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=(django_model_to_dict.mixins.ToDictMixin, models.Model),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.Project'),
            preserve_default=False,
        ),
    ]
