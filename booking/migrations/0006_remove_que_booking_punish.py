# Generated by Django 3.2.3 on 2021-06-17 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_que_booking_punish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='que_booking',
            name='punish',
        ),
    ]