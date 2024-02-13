# Generated by Django 5.0.2 on 2024-02-13 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("itinerary", "0004_rename_itinerary_day_itinerary"),
    ]

    operations = [
        migrations.AddField(
            model_name="places",
            name="content_type",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="places",
            name="object_id",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]