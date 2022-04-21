# Generated by Django 4.0.4 on 2022-04-20 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('start_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
