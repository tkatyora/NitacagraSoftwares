# Generated by Django 4.1.4 on 2022-12-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ourservices', '0019_alter_servicestable_oldprice_alter_servicestable_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicestable',
            name='section',
            field=models.CharField(choices=[('web', 'Web Developmnent'), ('desktop', 'Desktop Development'), ('mobile', 'Mobile Development'), ('network', 'Networking')], max_length=20, null=True),
        ),
    ]