# Generated by Django 4.1.4 on 2023-07-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_advertisment_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]