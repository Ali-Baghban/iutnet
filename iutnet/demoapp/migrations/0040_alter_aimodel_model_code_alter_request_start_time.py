# Generated by Django 4.2 on 2023-07-26 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0039_alter_aimodel_model_code_alter_request_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aimodel",
            name="model_code",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 26, 17, 26, 28, 918958), null=True
            ),
        ),
    ]
