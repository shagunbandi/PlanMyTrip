# Generated by Django 5.0.2 on 2024-02-14 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("itinerary", "0005_places_content_type_places_object_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="day",
            options={"ordering": ("order",)},
        ),
        migrations.AlterModelOptions(
            name="places",
            options={"ordering": ("order",)},
        ),
        migrations.AddField(
            model_name="day",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=0, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="places",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="itinerary",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
