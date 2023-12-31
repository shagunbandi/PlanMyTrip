# Generated by Django 4.2.6 on 2023-10-24 21:48

import common.enums
from django.db import migrations, models
import enumchoicefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_restaurant_options_alter_restaurant_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="reservation_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="reservation_file",
            field=models.FileField(blank=True, null=True, upload_to="reservations/"),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="reservation_link",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="reservation_place_id",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="reservation_status",
            field=enumchoicefield.fields.EnumChoiceField(
                default=common.enums.RESERVATION_STATUS["NO"],
                enum_class=common.enums.RESERVATION_STATUS,
                max_length=6,
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="reservation_time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
