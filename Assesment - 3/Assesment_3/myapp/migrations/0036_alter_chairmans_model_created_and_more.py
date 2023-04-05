# Generated by Django 4.1.5 on 2023-04-03 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_notices_model_notices_view_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 840523)),
        ),
        migrations.AlterField(
            model_name='events_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 840523)),
        ),
        migrations.AlterField(
            model_name='members_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 842517)),
        ),
        migrations.AlterField(
            model_name='notices_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 841521)),
        ),
        migrations.AlterField(
            model_name='notices_view_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 841521)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 842517)),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 844529)),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 841521)),
        ),
        migrations.AlterField(
            model_name='visitors_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 844529)),
        ),
        migrations.AlterField(
            model_name='watchmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 48, 18, 842517)),
        ),
    ]