# Generated by Django 3.0.5 on 2020-04-20 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('otp_messagebird', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagebirdsmsdevice',
            name='key',
        ),
        migrations.RemoveField(
            model_name='messagebirdsmsdevice',
            name='last_t',
        ),
        migrations.AddField(
            model_name='messagebirdsmsdevice',
            name='token',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='messagebirdsmsdevice',
            name='valid_until',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The timestamp of the moment of expiry of the saved token.'),
        ),
    ]
