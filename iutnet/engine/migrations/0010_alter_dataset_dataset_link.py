# Generated by Django 4.2 on 2023-06-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0009_alter_dataset_dataset_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="dataset_link",
            field=models.URLField(default="https://google.com", null=True),
        ),
    ]
