# Generated by Django 4.2.3 on 2023-07-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=50)),
                ('Addet_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
