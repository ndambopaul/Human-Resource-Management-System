# Generated by Django 5.0.6 on 2024-06-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0004_employeesalary_overtime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeeovertime",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=250, max_digits=100),
        ),
    ]