# Generated by Django 4.2.4 on 2023-09-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0008_alter_orders_items_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_items',
            name='order_status',
            field=models.IntegerField(default=25),
        ),
    ]
