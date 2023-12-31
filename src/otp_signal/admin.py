from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import SignalDevice


class SignalDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_signal.models.SignalDevice`.
    """

    fieldsets = [
        (
            "Identity",
            {
                "fields": ["user", "name", "confirmed"],
            },
        ),
        (
            "Configuration",
            {
                "fields": ["number"],
            },
        ),
    ]
    raw_id_fields = ["user"]


try:
    admin.site.register(SignalDevice, SignalDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass
