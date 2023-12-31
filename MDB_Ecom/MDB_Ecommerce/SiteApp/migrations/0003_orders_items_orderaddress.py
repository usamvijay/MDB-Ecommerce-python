# Generated by Django 4.2.4 on 2023-08-24 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0007_categories_slug_products_slug'),
        ('SiteApp', '0002_rename_user_cart_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('tracing_number', models.CharField(max_length=150, null=True)),
                ('created_At', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiteApp.user_data')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=500)),
                ('appartment', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=10)),
                ('payment', models.CharField(default=1, max_length=10)),
                ('Zip_code', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('created_At', models.DateField(auto_now=True)),
                ('Orders_id', models.CharField(max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SiteApp.user_data')),
            ],
        ),
    ]
