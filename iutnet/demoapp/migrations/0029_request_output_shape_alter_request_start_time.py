# Generated by Django 4.2 on 2023-07-15 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0028_alter_request_eeg_chan_alter_request_eog_chan_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="output_shape",
            field=models.CharField(default="(1000,3,250)", max_length=50),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 15, 16, 57, 33, 723487), null=True
            ),
        ),
    ]
