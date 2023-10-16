import logging

from django.core.exceptions import ImproperlyConfigured
from django.db import models

from django_otp.models import SideChannelDevice, ThrottlingMixin
import pysignalclirestapi

from .conf import settings


logger = logging.getLogger(__name__)


class SignalDevice(ThrottlingMixin, SideChannelDevice):
    """
    :class:`~django_otp.models.SideChannelDevice` that delivers tokens through the
    `Signal REST API <https://github.com/bbernhard/signal-cli-rest-api>`_ .

    The tokens are valid for :setting:`OTP_SIGNAL_TOKEN_VALIDITY` seconds.
    Once a token has been accepted, it is no longer valid.

    .. attribute:: number

        *CharField*: The mobile phone number to deliver to. This module requires
        using the `E.164 <http://en.wikipedia.org/wiki/E.164>`_ format. For US numbers,
        this would look like '+15555555555'.

    """

    number = models.CharField(
        max_length=30, help_text="The mobile number to deliver tokens to (E.164)."
    )

    class Meta(SideChannelDevice.Meta):
        verbose_name = "Signal Message Device"

    def get_throttle_factor(self):
        return settings.OTP_SIGNAL_THROTTLE_FACTOR

    def generate_challenge(self):
        """
        Generates a random token and sends it to ``self.number``.

        :returns: Challenge message on success.
        :raises: Exception if delivery fails.

        """
        self.generate_token(valid_secs=settings.OTP_SIGNAL_TOKEN_VALIDITY)

        message = self._get_token_message(self.token)

        if settings.OTP_SIGNAL_NO_DELIVERY:
            logger.info(message)
        else:
            self._deliver_token(message)

        challenge = self._get_challenge_message(self.token)

        return challenge

    def _validate_config(self):
        if settings.OTP_SIGNAL_API_SERVER is None:
            raise ImproperlyConfigured(
                "OTP_SIGNAL_API_SERVER must be set to your Signal REST API server"
            )

    def verify_token(self, token):
        verify_allowed, _ = self.verify_is_allowed()
        if verify_allowed:
            verified = super().verify_token(token)

            if verified:
                self.throttle_reset()
            else:
                self.throttle_increment()
        else:
            verified = False

        return verified

    def _get_token_message(self, token):
        token_template = getattr(settings, "OTP_SIGNAL_TOKEN_TEMPLATE", None)
        if callable(token_template):
            token_template = token_template(self)
        message = token_template.format(token=self.token)
        return message

    def _get_challenge_message(self, token):
        challenge_message = getattr(settings, "OTP_SIGNAL_CHALLENGE_MESSAGE", None)
        if callable(challenge_message):
            challenge_message = challenge_message(self)
        challenge = challenge_message.format(token=token)
        return challenge

    def _deliver_token(self, token):
        self._validate_config()

        client = pysignalclirestapi.SignalCliRestApi(
            base_url=getattr(settings, "OTP_SIGNAL_API_SERVER", None),
            number=getattr(settings, "OTP_SIGNAL_NUMBER", None),
            verify_ssl=getattr(settings, "OTP_SIGNAL_VERIFY_SSL", True),
        )
        try:
            client.send_message(message=str(token), recipients=[self.number])
        except pysignalclirestapi.SignalCliRestApiError as e:
            logger.exception("Error sending token via Signal: {0}".format(e))
            raise
