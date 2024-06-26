# Generated by Django 5.0.3 on 2024-04-09 19:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0017_alter_educationinformation_employee"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeDocument",
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
                (
                    "police_clearance",
                    models.FileField(
                        blank=True, null=True, upload_to="police_clearances/"
                    ),
                ),
                (
                    "chief_letter",
                    models.FileField(blank=True, null=True, upload_to="chief_letters/"),
                ),
                (
                    "recommendation_letter",
                    models.FileField(
                        blank=True, null=True, upload_to="recommended_letters/"
                    ),
                ),
                (
                    "scanned_id",
                    models.FileField(blank=True, null=True, upload_to="scanned_ids/"),
                ),
                (
                    "kcse_certificate",
                    models.FileField(null=True, upload_to="kcse_certificates/"),
                ),
                (
                    "kcpe_certificate",
                    models.FileField(null=True, upload_to="kcpe_certificates/"),
                ),
                (
                    "college_certificate",
                    models.FileField(null=True, upload_to="college_certificates/"),
                ),
                (
                    "kra_certificate",
                    models.FileField(null=True, upload_to="kra_certificates"),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employeedocuments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
