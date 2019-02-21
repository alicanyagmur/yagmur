# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-20 17:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_selection', models.DateField(max_length=20)),
                ('reservation_date', models.DateField(max_length=50)),
                ('start_time', models.TimeField(max_length=20)),
                ('end_time', models.TimeField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Reservation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
