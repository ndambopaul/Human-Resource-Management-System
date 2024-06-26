# Generated by Django 5.0.3 on 2024-03-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipments", "0003_equipmentissue_issued_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipmentissue",
            name="status",
            field=models.CharField(
                choices=[
                    ("Returned", "Returned"),
                    ("Pending Return", "Pending Return"),
                    ("Lost", "Lost"),
                    ("Returned Late", "Returned Late"),
                ],
                max_length=255,
            ),
        ),
    ]
