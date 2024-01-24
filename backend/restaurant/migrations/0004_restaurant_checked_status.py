# Generated by Django 4.2.6 on 2024-01-23 23:03

import common.enums
from django.db import migrations
import enumchoicefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_restaurant_reservation_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="checked_status",
            field=enumchoicefield.fields.EnumChoiceField(
                default=common.enums.CHECKED_STATUS["UNSELECTED"],
                enum_class=common.enums.CHECKED_STATUS,
                max_length=10,
            ),
        ),
    ]
