# Generated by Django 4.1.5 on 2023-04-03 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_alter_event_model_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 45, 36, 98391)),
        ),
    ]
