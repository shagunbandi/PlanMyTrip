# Generated by Django 5.0.2 on 2024-02-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("itinerary", "0011_remove_day_text_place_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="day",
            name="title",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
