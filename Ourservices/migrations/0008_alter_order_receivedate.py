# Generated by Django 4.1.1 on 2022-12-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0007_customers_phonenumber_alter_customers_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ReceiveDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
