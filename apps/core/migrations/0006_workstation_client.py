# Generated by Django 5.0.3 on 2024-04-11 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_workstation_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="workstation",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="workstations",
                to="core.client",
            ),
        ),
    ]
