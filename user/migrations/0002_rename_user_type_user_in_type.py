# Generated by Django 3.2.3 on 2021-06-11 04:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_type',
            new_name='User_in_type',
        ),
    ]