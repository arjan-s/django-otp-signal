django-otp-messagebird
=================

.. include:: ../../README.rst


Installation
------------

django-otp-messagebird can be installed via pip::

    pip install django-otp-messagebird


Once installed it should be added to INSTALLED_APPS after django_otp core::

    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        'django_otp.plugins.otp_hotp',
        'django_otp.plugins.otp_static',

        'otp_messagebird',
    ]


MessageBird SMS Devices
------------------

.. autoclass:: otp_messageBird.models.MessageBirdSMSDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclass is registered
with the default admin site. We recommend its use with custom admin sites as
well:

.. autoclass:: otp_messagebird.admin.MessageBirdSMSDeviceAdmin


Settings
--------

.. setting:: OTP_MESSAGEBIRD_ACCESS_KEY

**OTP_MESSAGEBIRD_ACCESS_KEY**

Default: ``None``

Your MessageBird API key.


.. setting:: OTP_MESSAGEBIRD_SMS_CHALLENGE_MESSAGE

**OTP_MESSAGEBIRD_SMS_CHALLENGE_MESSAGE**

Default: ``"Sent by SMS"``

The message returned by
:meth:`~otp_messagebird.models.MessageBirdSMSDevice.generate_challenge`. This may contain
``'{token}'``, which will be replaced by the token. This completely negates any
security benefit to the device, but it's handy for development, especially in
combination with :setting:`OTP_MESSAGEBIRD_NO_DELIVERY`.


.. setting:: OTP_MESSAGEBIRD_VOICE_CHALLENGE_MESSAGE

**OTP_MESSAGEBIRD_VOICE_CHALLENGE_MESSAGE**

Default: ``"Phone call initiated"``

The message returned by
:meth:`~otp_messagebird.models.MessageBirdVoiceDevice.generate_challenge`. This may contain
``'{token}'``, which will be replaced by the token. This completely negates any
security benefit to the device, but it's handy for development, especially in
combination with :setting:`OTP_MESSAGEBIRD_NO_DELIVERY`.


.. setting:: OTP_MESSAGEBIRD_FROM

**OTP_MESSAGEBIRD_FROM**

Default: ``None``

A string containing the sender of the SMS, with a maximum length of 11 characters.


.. setting:: OTP_MESSAGEBIRD_NO_DELIVERY

**OTP_MESSAGEBIRD_NO_DELIVERY**

Default: ``False``

Send tokens to the 'otp_messagebird.models' logger instead of delivering them by SMS.
Useful for development.


.. setting:: OTP_MESSAGEBIRD_SMS_TOKEN_TEMPLATE

**OTP_MESSAGEBIRD_SMS_TOKEN_TEMPLATE**

Default: ``"{token}"``

A string template for generating the token SMS message. By default, this is just the
token itself, but you can customize it. The template will be rendered with
Python string formatting (``template.format(token=token)``).


.. setting:: OTP_MESSAGEBIRD_VOICE_TOKEN_TEMPLATE

**OTP_MESSAGEBIRD_VOICE_TOKEN_TEMPLATE**

Default: ``"{token}"``

A string template for generating the token voice message. By default, this is just the
token itself, but you can customize it. The template will be rendered with
Python string formatting (``template.format(token=token)``).


.. setting:: OTP_MESSAGEBIRD_TOKEN_VALIDITY

**OTP_MESSAGEBIRD_TOKEN_VALIDITY**

Default: ``30``

The number of seconds for which a delivered token will be valid.


.. setting:: OTP_MESSAGEBIRD_THROTTLE_FACTOR

**OTP_MESSAGEBIRD_THROTTLE_FACTOR**

Default: ``1``

This controls the rate of throttling. The sequence of 1, 2, 4, 8... seconds is
multiplied by this factor to define the delay imposed after 1, 2, 3, 4...
successive failures. Set to ``0`` to disable throttling completely.


Changes
-------

:doc:`changes`


License
-------

.. include:: ../../LICENSE
