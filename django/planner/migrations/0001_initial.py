# Generated by Django 4.2.3 on 2023-07-20 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryCompound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64, null=True)),
                ('category', models.CharField(max_length=64, null=True)),
                ('activity_time_in_mins', models.IntegerField(default=-1)),
                ('rating_value', models.FloatField(null=True)),
                ('rating_count', models.IntegerField(null=True)),
                ('duration_in_mins', models.FloatField(null=True)),
                ('distance_in_meters', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('nth_day', models.IntegerField(null=True)),
                ('activity_number', models.IntegerField(null=True)),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.itinerarycompound')),
            ],
        ),
    ]
