# Generated by Django 4.2.7 on 2023-11-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0011_rename_item_purchase_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.CharField(default='pending', max_length=200),
        ),
    ]
