# Generated by Django 4.2 on 2023-07-12 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0012_remove_request_ai_model_remove_request_dataset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="end_time",
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 16, 52, 24, 512918), null=True
            ),
        ),
    ]