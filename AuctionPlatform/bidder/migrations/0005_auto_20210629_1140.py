# Generated by Django 2.1.7 on 2021-06-29 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidder', '0004_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='bid_id',
            new_name='bid',
        ),
    ]
