# Generated by Django 5.0.3 on 2024-03-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workstation",
            name="country",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="workstation",
            name="county",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="workstation",
            name="postal_address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="workstation",
            name="town",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
