# Generated by Django 4.2.6 on 2023-10-25 07:45

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SignalDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The human-readable name of this device.",
                        max_length=64,
                    ),
                ),
                (
                    "confirmed",
                    models.BooleanField(
                        default=True, help_text="Is this device ready for use?"
                    ),
                ),
                ("token", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "valid_until",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="The timestamp of the moment of expiry of the saved token.",
                    ),
                ),
                (
                    "throttling_failure_timestamp",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        help_text="A timestamp of the last failed verification attempt. Null if last attempt succeeded.",
                        null=True,
                    ),
                ),
                (
                    "throttling_failure_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Number of successive failed attempts."
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        help_text="The mobile number to deliver tokens to (E.164).",
                        max_length=30,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user that this device belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Signal Message Device",
                "abstract": False,
            },
        ),
    ]
