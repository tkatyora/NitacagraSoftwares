# Generated by Django 4.1.4 on 2023-04-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_remove_contentcreater_user_nitacagrausers_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nitacagrausers',
            old_name='user',
            new_name='personalInfo',
        ),
    ]