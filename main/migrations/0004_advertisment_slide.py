# Generated by Django 4.1.4 on 2023-07-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_advertisment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='slide',
            field=models.CharField(max_length=50, null=True, verbose_name='slide number'),
        ),
    ]
