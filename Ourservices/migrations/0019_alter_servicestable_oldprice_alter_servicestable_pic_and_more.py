# Generated by Django 4.1.4 on 2022-12-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0018_remove_order_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicestable',
            name='oldPrice',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='servicestable',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='servicestable',
            name='section',
            field=models.CharField(choices=[('web', 'Web Developmnent'), ('desktop', 'Desktop Development'), ('mobile', 'Mobile Development'), ('ntewk', 'Networking')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='servicestable',
            name='specialOffer',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
