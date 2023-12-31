# Generated by Django 4.2.4 on 2023-09-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0009_alter_orders_items_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders_items',
            name='order_status',
            field=models.IntegerField(choices=[(20, 'Pending'), (40, 'Confirmed'), (60, 'Shipped'), (80, 'Our for Delevery'), (100, 'Delevered'), (0, 'Cancel')], default=25),
        ),
    ]
