# Generated by Django 5.0.6 on 2024-06-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_user_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending Approval", "Pending Approval"),
                    ("Declined", "Declined"),
                    ("Available", "Available"),
                    ("On Leave", "On Leave"),
                    ("Suspended", "Suspended"),
                ],
                default="Available",
                max_length=255,
            ),
        ),
    ]