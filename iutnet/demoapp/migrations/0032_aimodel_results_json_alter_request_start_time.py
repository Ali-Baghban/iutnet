# Generated by Django 4.2 on 2023-07-24 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0031_alter_aimodel_related_paper_alter_request_start_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="aimodel",
            name="results_json",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 24, 16, 43, 50, 932319), null=True
            ),
        ),
    ]