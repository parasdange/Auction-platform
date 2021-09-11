# Generated by Django 2.1.7 on 2021-06-07 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('qty', models.IntegerField()),
                ('city', models.IntegerField()),
                ('des', models.CharField(max_length=200)),
                ('closing_date', models.CharField(max_length=20)),
                ('cover_img', models.ImageField(blank=True, upload_to='product_image')),
                ('current_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_images', models.ImageField(blank=True, upload_to='product_image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Product')),
            ],
        ),
    ]