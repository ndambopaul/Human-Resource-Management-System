# Generated by Django 5.0.6 on 2024-06-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_rename_nssf_number_user_kra_pin"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="nssf_number",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
