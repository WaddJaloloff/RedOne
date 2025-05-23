# Generated by Django 4.2 on 2025-04-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename_price_product_price1_product_price2_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="about",
            new_name="about_ru",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="name",
            new_name="name_ru",
        ),
        migrations.AddField(
            model_name="product",
            name="about_uz",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="name_uz",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
