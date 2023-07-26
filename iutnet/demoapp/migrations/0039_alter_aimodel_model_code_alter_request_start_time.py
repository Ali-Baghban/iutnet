# Generated by Django 4.2 on 2023-07-26 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0038_alter_request_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aimodel",
            name="model_code",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 26, 17, 25, 2, 273110), null=True
            ),
        ),
    ]
