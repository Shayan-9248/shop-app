# Generated by Django 3.1.7 on 2021-03-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_product', '0012_auto_20210301_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sell',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variant',
            name='sell',
            field=models.PositiveIntegerField(default=0),
        ),
    ]