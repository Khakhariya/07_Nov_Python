# Generated by Django 4.1.5 on 2023-02-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_mst_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('Product_model', models.CharField(max_length=10)),
                ('Product_price', models.IntegerField()),
                ('Product_image', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]
