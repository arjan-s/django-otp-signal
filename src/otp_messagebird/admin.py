from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import MessageBirdSMSDevice, MessageBirdVoiceDevice


class MessageBirdSMSDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_messagebird.models.MessageBirdSMSDevice`.
    """

    fieldsets = [
        ("Identity", {"fields": ["user", "name", "confirmed"], }),
        ("Configuration", {"fields": ["number"], }),
    ]
    raw_id_fields = ["user"]


try:
    admin.site.register(MessageBirdSMSDevice, MessageBirdSMSDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass


class MessageBirdVoiceDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_messagebird.models.MessageBirdVoiceDevice`.
    """

    fieldsets = [
        ("Identity", {"fields": ["user", "name", "confirmed"], }),
        ("Configuration", {"fields": ["number", "language"], }),
    ]
    raw_id_fields = ["user"]


try:
    admin.site.register(MessageBirdVoiceDevice, MessageBirdVoiceDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass
