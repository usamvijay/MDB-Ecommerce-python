# Generated by Django 4.2.4 on 2023-08-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0003_orders_items_orderaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_items',
            old_name='tracing_number',
            new_name='Orders_id',
        ),
        migrations.RemoveField(
            model_name='orderaddress',
            name='payment',
        ),
        migrations.AlterField(
            model_name='orderaddress',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
    ]