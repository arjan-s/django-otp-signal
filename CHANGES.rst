v0.2.1 - August 05, 2020 - Throttling
---------------------------------------------

Add token verification throttling to MessageBirdBaseDevice.


v0.2.0 - June 17, 2020 - Voice device
---------------------------------------------

Add MessageBirdVoiceDevice which calls the user and reads the body to them.
Rebased on SideChannelDevice from django-otp.


v0.1.2 - February 10, 2020 - Dynamic settings
---------------------------------------------

Made token template and challenge message dynamic, inspired by the same change
in django-otp.


v0.1.1 - December 12, 2019 - Missing dependency
-----------------------------------------------

Added missing dependency messagebird.
Fixed source link badge in readme.


v0.1.0 - December 9, 2019 - Initial release
-------------------------------------------

Cloned django-otp-twilio v0.5.1 and renamed to django-otp-messagebird.
Use MessageBird API instead of Twilio API.
