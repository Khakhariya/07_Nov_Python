# Generated by Django 4.1.5 on 2023-03-06 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_watchmans_model_alter_chairmans_model_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 450620)),
        ),
        migrations.AlterField(
            model_name='events_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 450620)),
        ),
        migrations.AlterField(
            model_name='members_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 451620)),
        ),
        migrations.AlterField(
            model_name='notices_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 450620)),
        ),
        migrations.AlterField(
            model_name='notices_view_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 450620)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 451620)),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 450620)),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 451620)),
        ),
        migrations.AlterField(
            model_name='visitors_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 451620)),
        ),
        migrations.AlterField(
            model_name='watchmans_model',
            name='cate',
            field=models.CharField(default='watchman', max_length=15),
        ),
        migrations.AlterField(
            model_name='watchmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 18, 33, 451620)),
        ),
    ]
