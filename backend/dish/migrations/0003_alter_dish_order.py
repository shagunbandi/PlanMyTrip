# Generated by Django 4.2.6 on 2023-10-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0002_alter_dish_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, editable=False, verbose_name="order"
            ),
        ),
    ]
