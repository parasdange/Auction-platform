# Generated by Django 2.1.7 on 2021-06-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210607_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_img',
            field=models.ImageField(blank=True, upload_to='productImage'),
        ),
    ]
