# Generated by Django 5.0.6 on 2024-06-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0003_employeeovertime"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeesalary",
            name="overtime",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
