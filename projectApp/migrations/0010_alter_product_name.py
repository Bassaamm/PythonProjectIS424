# Generated by Django 4.2.7 on 2023-11-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0009_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
