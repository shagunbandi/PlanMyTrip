# Generated by Django 4.2.6 on 2023-10-21 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import experience.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("itinerary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=60)),
                ("description", models.CharField(max_length=180)),
                (
                    "type",
                    enumchoicefield.fields.EnumChoiceField(
                        default=experience.models.ExperienceTypes(4),
                        enum_class=experience.models.ExperienceTypes,
                        max_length=10,
                    ),
                ),
                ("google_place_id", models.CharField(max_length=120, null=True)),
                (
                    "ticket_link",
                    models.CharField(blank=True, max_length=180, null=True),
                ),
                (
                    "reservation_link",
                    models.CharField(blank=True, max_length=180, null=True),
                ),
                ("activity_start_time", models.DateTimeField(blank=True, null=True)),
                ("activity_end_time", models.DateTimeField(blank=True, null=True)),
                ("order", models.IntegerField()),
                (
                    "itinerary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="itinerary.itinerary",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "itinerary")},
            },
        ),
    ]
