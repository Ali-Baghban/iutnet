# Generated by Django 4.2 on 2023-09-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0047_alter_request_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="start_time",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]