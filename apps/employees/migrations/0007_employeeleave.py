# Generated by Django 5.0.3 on 2024-03-28 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0006_rename_checked_in_attendance_marked"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeLeave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("days_applied", models.IntegerField(default=1)),
                (
                    "leave_type",
                    models.CharField(
                        choices=[
                            ("Paid Leave", "Paid Leave"),
                            ("Unpaid Leave", "Unpaid Leave"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                            ("Pending Review", "Pending Review"),
                        ],
                        default="Pending Review",
                        max_length=255,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
