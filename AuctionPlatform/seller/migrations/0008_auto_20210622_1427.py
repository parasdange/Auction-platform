# Generated by Django 2.1.7 on 2021-06-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_auto_20210616_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.CharField(max_length=700),
        ),
    ]