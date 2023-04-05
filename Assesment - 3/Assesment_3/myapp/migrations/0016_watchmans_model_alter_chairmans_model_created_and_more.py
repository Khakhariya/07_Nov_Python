# Generated by Django 4.1.5 on 2023-03-06 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_delete_watchmans_model_alter_chairmans_model_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='watchmans_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 248594))),
                ('cate', models.CharField(max_length=15)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('Mobile', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='chairmans_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 245957)),
        ),
        migrations.AlterField(
            model_name='events_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 245957)),
        ),
        migrations.AlterField(
            model_name='members_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 251037)),
        ),
        migrations.AlterField(
            model_name='notices_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 247594)),
        ),
        migrations.AlterField(
            model_name='notices_view_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 246955)),
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 251037)),
        ),
        migrations.AlterField(
            model_name='transactions_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 247594)),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 248594)),
        ),
        migrations.AlterField(
            model_name='visitors_model',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 6, 18, 11, 22, 248594)),
        ),
    ]
