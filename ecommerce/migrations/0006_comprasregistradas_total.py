# Generated by Django 4.2.7 on 2023-12-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_sliderspromocionales'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasregistradas',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
