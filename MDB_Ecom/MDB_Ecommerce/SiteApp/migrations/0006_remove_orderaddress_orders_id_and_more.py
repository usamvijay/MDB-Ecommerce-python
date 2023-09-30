# Generated by Django 4.2.4 on 2023-08-31 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0005_orders_items_orders_status_orders_items_updatedat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderaddress',
            name='Orders_id',
        ),
        migrations.RemoveField(
            model_name='orders_items',
            name='Orders_Status',
        ),
        migrations.AddField(
            model_name='orders_items',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteApp.orderaddress'),
        ),
        migrations.AddField(
            model_name='orders_items',
            name='color',
            field=models.CharField(max_length=150, null=True),
        ),
    ]