# Generated by Django 4.2.3 on 2023-07-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0002_categories_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='Category_icon',
            field=models.ImageField(default='null', upload_to='media/Categories/'),
        ),
    ]
