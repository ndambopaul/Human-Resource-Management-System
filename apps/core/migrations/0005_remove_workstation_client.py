# Generated by Django 5.0.3 on 2024-04-11 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_workstation_client"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workstation",
            name="client",
        ),
    ]
