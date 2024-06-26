# Generated by Django 5.0.6 on 2024-06-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_paymentconfig"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaxBand",
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
                    "category",
                    models.CharField(
                        choices=[
                            ("1st Band", "1st Band"),
                            ("2nd Band", "2nd Band"),
                            ("3rd Band", "3rd Band"),
                        ],
                        max_length=255,
                    ),
                ),
                ("lower_end", models.DecimalField(decimal_places=2, max_digits=100)),
                ("upper_end", models.DecimalField(decimal_places=2, max_digits=100)),
                ("nhif", models.DecimalField(decimal_places=2, max_digits=100)),
                ("shif", models.DecimalField(decimal_places=2, max_digits=100)),
                (
                    "nssf_tier_one",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
                (
                    "nssf_tier_two",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
                ("housing_levy", models.DecimalField(decimal_places=2, max_digits=10)),
                ("tax_relief", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "allowable_deductions",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
                (
                    "insurance_relief",
                    models.DecimalField(decimal_places=2, max_digits=100),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
