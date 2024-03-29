# Generated by Django 4.2 on 2023-07-15 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0024_request_stim_chan_request_event_from_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="montage_type",
            field=models.CharField(
                choices=[
                    (False, "None"),
                    ("standard_1005", "standard_1005"),
                    ("standard_1020", "standard_1020"),
                ],
                default="standard_1020",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="request",
            name="on_missing",
            field=models.CharField(
                choices=[("Warn", "warn"), ("x", "x")], default="Warn", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="montage",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 15, 16, 4, 57, 415420), null=True
            ),
        ),
    ]
