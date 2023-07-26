# Generated by Django 4.2 on 2023-07-26 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0036_alter_aimodel_name_alter_request_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aimodel",
            name="model_code",
            field=models.TextField(blank=True, default=None, editable=False),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 26, 17, 20, 8, 458542), null=True
            ),
        ),
    ]
