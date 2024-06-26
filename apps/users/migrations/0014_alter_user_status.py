# Generated by Django 5.0.6 on 2024-06-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_user_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending Approval", "Pending Approval"),
                    ("Available", "Available"),
                    ("On Leave", "On Leave"),
                    ("Suspended", "Suspended"),
                ],
                default="Available",
                max_length=255,
            ),
        ),
    ]
