# Generated by Django 3.0.5 on 2020-07-12 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20200712_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 19, 21, 43, 306245), verbose_name='Due Date'),
        ),
    ]
