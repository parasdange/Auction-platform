# Generated by Django 2.1.7 on 2021-06-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20210608_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='product_images',
            field=models.ImageField(blank=True, upload_to='productImage'),
        ),
    ]
