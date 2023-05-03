# Generated by Django 4.1.1 on 2022-11-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Service', models.CharField(max_length=50)),
                ('ReceiveDate', models.DateTimeField()),
                ('SubmitDate', models.DateTimeField()),
            ],
        ),
    ]
