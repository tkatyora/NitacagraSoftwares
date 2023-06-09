# Generated by Django 4.1.4 on 2023-02-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0022_alter_customers_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicestable',
            options={'ordering': ('-created_on',)},
        ),
        migrations.AddField(
            model_name='servicestable',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='servicestable',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicestable',
            name='newPrice',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='servicestable',
            name='oldPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
