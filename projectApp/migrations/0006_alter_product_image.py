# Generated by Django 4.2.5 on 2023-11-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_alter_product_image_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
