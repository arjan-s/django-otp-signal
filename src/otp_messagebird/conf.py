import django.conf
import django.test.utils


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default
    values if they are not specified by the configuration.
    """

    _defaults = {
        "OTP_MESSAGEBIRD_ACCESS_KEY": None,
        "OTP_MESSAGEBIRD_SMS_CHALLENGE_MESSAGE": "Sent by SMS",
        "OTP_MESSAGEBIRD_VOICE_CHALLENGE_MESSAGE": "Phone call initiated",
        "OTP_MESSAGEBIRD_FROM": None,
        "OTP_MESSAGEBIRD_NO_DELIVERY": False,
        "OTP_MESSAGEBIRD_SMS_TOKEN_TEMPLATE": "{token}",
        "OTP_MESSAGEBIRD_VOICE_TOKEN_TEMPLATE": "{token}",
        "OTP_MESSAGEBIRD_TOKEN_VALIDITY": 30,
        "OTP_MESSAGEBIRD_THROTTLE_FACTOR": 1,
    }

    def __getattr__(self, name):
        if hasattr(django.conf.settings, name):
            value = getattr(django.conf.settings, name)
        elif name in self._defaults:
            value = self._defaults[name]
        else:
            raise AttributeError(name)

        return value


settings = Settings()
