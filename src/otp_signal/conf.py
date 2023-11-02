import django.conf
import django.test.utils


class Settings:
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default
    values if they are not specified by the configuration.
    """

    _defaults = {
        "OTP_SIGNAL_API_SERVER": None,
        "OTP_SIGNAL_NUMBER": None,
        "OTP_SIGNAL_CHALLENGE_MESSAGE": "Sent via Signal",
        "OTP_SIGNAL_VERIFY_SSL": True,
        "OTP_SIGNAL_NO_DELIVERY": False,
        "OTP_SIGNAL_TOKEN_TEMPLATE": "{token}",
        "OTP_SIGNAL_TOKEN_VALIDITY": 30,
        "OTP_SIGNAL_THROTTLE_FACTOR": 1,
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
