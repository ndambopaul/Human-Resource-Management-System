# Generated by Django 5.0.3 on 2024-03-28 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0008_employeeleave_leave_from_employeeleave_leave_to"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeleave",
            name="approved_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leaveapprovers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
