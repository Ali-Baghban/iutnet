# Generated by Django 4.2 on 2023-07-15 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0022_request_eeg_chan_request_eog_chan_request_baseline_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="baseline",
            field=models.CharField(default="None", max_length=20),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 15, 15, 52, 31, 375257), null=True
            ),
        ),
    ]