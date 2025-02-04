# Generated by Django 4.2 on 2025-02-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_features", "0006_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="categoryimage/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(),
        ),
    ]
