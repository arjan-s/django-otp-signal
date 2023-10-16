# Generated by Django 3.0 on 2019-12-09 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

import otp_messagebird.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBirdSMSDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text='Is this device ready for use?')),
                ('number', models.CharField(help_text='The mobile number to deliver tokens to (E.164).', max_length=30)),
                ('key', models.CharField(default=otp_messagebird.models.default_key, help_text='A random key used to generate tokens (hex-encoded).', max_length=40, validators=[otp_messagebird.models.key_validator])),
                ('last_t', models.BigIntegerField(default=-1, help_text='The t value of the latest verified token. The next token must be at a higher time step.')),
                ('user', models.ForeignKey(help_text='The user that this device belongs to.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MessageBird SMS Device',
                'abstract': False,
            },
        ),
    ]
