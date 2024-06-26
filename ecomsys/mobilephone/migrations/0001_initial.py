# Generated by Django 5.0.3 on 2024-04-01 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('image', models.ImageField(upload_to='mobile_phone_images/')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
