# Generated by Django 4.2 on 2025-05-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_alter_product_category_alter_topproduct_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name_ru",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
