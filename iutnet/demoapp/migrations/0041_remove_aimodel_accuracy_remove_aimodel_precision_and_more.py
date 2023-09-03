# Generated by Django 4.2 on 2023-09-01 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0040_alter_aimodel_model_code_alter_request_start_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aimodel",
            name="accuracy",
        ),
        migrations.RemoveField(
            model_name="aimodel",
            name="precision",
        ),
        migrations.RemoveField(
            model_name="aimodel",
            name="recall",
        ),
        migrations.RemoveField(
            model_name="aimodel",
            name="results_json",
        ),
        migrations.AddField(
            model_name="request",
            name="accuracy",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="request",
            name="precision",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="request",
            name="private",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="request",
            name="recall",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="request",
            name="results_json",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 1, 14, 20, 12, 106855), null=True
            ),
        ),
    ]
