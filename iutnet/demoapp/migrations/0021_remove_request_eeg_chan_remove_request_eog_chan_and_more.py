# Generated by Django 4.2 on 2023-07-15 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0020_request_eeg_chan_request_eog_chan_request_baseline_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="request",
            name="EEG_Chan",
        ),
        migrations.RemoveField(
            model_name="request",
            name="EOG_Chan",
        ),
        migrations.RemoveField(
            model_name="request",
            name="baseline",
        ),
        migrations.RemoveField(
            model_name="request",
            name="event_id",
        ),
        migrations.RemoveField(
            model_name="request",
            name="exclude",
        ),
        migrations.RemoveField(
            model_name="request",
            name="filter",
        ),
        migrations.RemoveField(
            model_name="request",
            name="high_band",
        ),
        migrations.RemoveField(
            model_name="request",
            name="low_band",
        ),
        migrations.RemoveField(
            model_name="request",
            name="montage",
        ),
        migrations.RemoveField(
            model_name="request",
            name="projection",
        ),
        migrations.RemoveField(
            model_name="request",
            name="test_size",
        ),
        migrations.RemoveField(
            model_name="request",
            name="tmax",
        ),
        migrations.RemoveField(
            model_name="request",
            name="tmin",
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 15, 15, 49, 54, 457590), null=True
            ),
        ),
    ]
