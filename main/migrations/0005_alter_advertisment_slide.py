# Generated by Django 4.1.4 on 2023-07-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_advertisment_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='slide',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], max_length=50, null=True, verbose_name='slide number'),
        ),
    ]
