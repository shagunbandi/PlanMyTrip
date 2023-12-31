# Generated by Django 4.2.6 on 2023-10-24 21:48

import common.enums
from django.db import migrations, models
import enumchoicefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("accomodation", "0002_alter_accomodation_options_alter_accomodation_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="accomodation",
            name="reservation_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="accomodation",
            name="reservation_file",
            field=models.FileField(blank=True, null=True, upload_to="reservations/"),
        ),
        migrations.AddField(
            model_name="accomodation",
            name="reservation_link",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="accomodation",
            name="reservation_place_id",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="accomodation",
            name="reservation_status",
            field=enumchoicefield.fields.EnumChoiceField(
                default=common.enums.RESERVATION_STATUS["NO"],
                enum_class=common.enums.RESERVATION_STATUS,
                max_length=6,
            ),
        ),
        migrations.AddField(
            model_name="accomodation",
            name="reservation_time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
