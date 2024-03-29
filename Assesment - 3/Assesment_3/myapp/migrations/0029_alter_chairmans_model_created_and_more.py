# Generated by Django 4.1.5 on 2023-03-07 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_chairmans_model_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 315762)),
        ),
        migrations.AlterField(
            model_name='events_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 315762)),
        ),
        migrations.AlterField(
            model_name='members_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 318683)),
        ),
        migrations.AlterField(
            model_name='notices_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 316838)),
        ),
        migrations.AlterField(
            model_name='notices_view_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 316838)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 318683)),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 316838)),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 316838)),
        ),
        migrations.AlterField(
            model_name='visitors_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 319762)),
        ),
        migrations.AlterField(
            model_name='visitors_model',
            name='out_time',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='watchmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 7, 10, 55, 8, 316838)),
        ),
    ]
