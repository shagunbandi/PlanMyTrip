# Generated by Django 5.0.2 on 2024-03-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plan", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="agenda",
            options={"ordering": ("is_itinerary", "order")},
        ),
        migrations.AddField(
            model_name="agenda",
            name="is_itinerary",
            field=models.BooleanField(default=False),
        ),
    ]