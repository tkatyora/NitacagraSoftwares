# Generated by Django 4.1.4 on 2022-12-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0021_customers_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Account',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
