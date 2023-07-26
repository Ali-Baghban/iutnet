# Generated by Django 4.2 on 2023-07-17 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0030_alter_aimodel_model_alter_aimodel_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aimodel",
            name="related_paper",
            field=models.ManyToManyField(blank=True, to="demoapp.paper"),
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 17, 17, 30, 16, 660633), null=True
            ),
        ),
    ]
