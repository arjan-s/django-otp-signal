django-otp-signal
=================

.. include:: ../../README.rst


Installation
------------

django-otp-signal can be installed via pip::

    pip install django-otp-signal


Once installed it should be added to INSTALLED_APPS after django_otp core::

    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        'django_otp.plugins.otp_hotp',
        'django_otp.plugins.otp_static',

        'otp_signal',
    ]


Signal Devices
--------------

.. autoclass:: otp_signal.models.SignalDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclass is registered
with the default admin site. We recommend its use with custom admin sites as
well:

.. autoclass:: otp_signal.admin.SignalDeviceAdmin


Settings
--------

.. setting:: OTP_SIGNAL_API_SERVER

**OTP_SIGNAL_API_SERVER**

Default: ``None``

Base URL of the Signal CLI REST API server.


.. setting:: OTP_SIGNAL_NUMBER

**OTP_SIGNAL_NUMBER**

Default: ``None``

The mobile phone number registered with Signal.


.. setting:: OTP_SIGNAL_VERIFY_SSL

**OTP_SIGNAL_VERIFY_SSL**

Default: ``True``

Tells the `requests` module whether to verify the HTTPS certificate or not.


.. setting:: OTP_SIGNAL_CHALLENGE_MESSAGE

**OTP_SIGNAL_CHALLENGE_MESSAGE**

Default: ``"Sent by Signal"``

The message returned by
:meth:`~otp_signal.models.SignalDevice.generate_challenge`. This may contain
``'{token}'``, which will be replaced by the token. This completely negates any
security benefit to the device, but it's handy for development, especially in
combination with :setting:`OTP_SIGNAL_NO_DELIVERY`.


.. setting:: OTP_SIGNAL_NO_DELIVERY

**OTP_SIGNAL_NO_DELIVERY**

Default: ``False``

Send tokens to the 'otp_signal.models' logger instead of delivering them by Signal.
Useful for development.


.. setting:: OTP_SIGNAL_TOKEN_TEMPLATE

**OTP_SIGNAL_TOKEN_TEMPLATE**

Default: ``"{token}"``

A string template for generating the token message. By default, this is just the
token itself, but you can customize it. The template will be rendered with
Python string formatting (``template.format(token=token)``).


.. setting:: OTP_SIGNAL_TOKEN_VALIDITY

**OTP_SIGNAL_TOKEN_VALIDITY**

Default: ``30``

The number of seconds for which a delivered token will be valid.


.. setting:: OTP_SIGNAL_THROTTLE_FACTOR

**OTP_SIGNAL_THROTTLE_FACTOR**

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
