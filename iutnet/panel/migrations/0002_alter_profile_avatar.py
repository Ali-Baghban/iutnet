# Generated by Django 4.2 on 2023-05-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="profile_images/default.png", upload_to="profile_images/"
            ),
        ),
    ]
