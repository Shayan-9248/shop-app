# Generated by Django 3.1.7 on 2021-03-01 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_order', '0004_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='title',
            new_name='code',
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]