# Generated by Django 4.1.5 on 2023-03-25 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 25, 17, 42, 50, 282661)),
        ),
    ]
