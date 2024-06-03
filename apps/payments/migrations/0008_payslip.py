# Generated by Django 5.0.6 on 2024-06-03 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0007_alter_employeesalary_daily_rate"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payslip",
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
                    "month",
                    models.CharField(
                        choices=[
                            ("January", "January"),
                            ("February", "February"),
                            ("March", "March"),
                            ("April", "April"),
                            ("May", "May"),
                            ("June", "June"),
                            ("July", "July"),
                            ("August", "August"),
                            ("September", "September"),
                            ("October", "October"),
                            ("November", "November"),
                            ("December", "December"),
                        ],
                        max_length=255,
                    ),
                ),
                ("year", models.CharField(max_length=10)),
                ("days_worked", models.IntegerField(default=0)),
                ("daily_rate", models.DecimalField(decimal_places=2, max_digits=100)),
                (
                    "overtime",
                    models.DecimalField(decimal_places=2, default=0, max_digits=100),
                ),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=100)),
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
