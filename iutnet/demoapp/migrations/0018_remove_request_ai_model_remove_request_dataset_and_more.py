# Generated by Django 4.2 on 2023-07-12 13:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0004_alter_profile_phone"),
        ("demoapp", "0017_request_end_time_request_start_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="request",
            name="ai_model",
        ),
        migrations.RemoveField(
            model_name="request",
            name="dataset",
        ),
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 12, 17, 4, 29, 483355), null=True
            ),
        ),
        migrations.RemoveField(
            model_name="request",
            name="user",
        ),
        migrations.AddField(
            model_name="request",
            name="ai_model",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="demoapp.aimodel",
            ),
        ),
        migrations.AddField(
            model_name="request",
            name="dataset",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="demoapp.dataset",
            ),
        ),
        migrations.AddField(
            model_name="request",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="demo_request",
                to="panel.profile",
            ),
        ),
    ]
