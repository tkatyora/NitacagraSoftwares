# Generated by Django 4.1.1 on 2022-12-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0016_remove_order_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='section',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
