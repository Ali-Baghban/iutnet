# Generated by Django 4.2 on 2023-06-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0006_remove_dataset_data_dataset_dataset_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="dataset_link",
            field=models.URLField(default=None),
        ),
    ]