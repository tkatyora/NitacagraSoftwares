# Generated by Django 4.1.4 on 2023-03-18 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0007_rename_companycode_contentcreater_companynumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NitacagraUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('nitacagraName', models.CharField(blank=True, choices=[('customer', 'customer'), ('murimi', 'murimiwangu'), ('creater', 'contentCreater')], max_length=50, null=True)),
                ('logInRole', models.CharField(choices=[('Customer', 'Customer'), ('murimi', 'MurimiWangu'), ('vendor', 'Ventor')], max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='contentcreater',
            name='location',
        ),
        migrations.RemoveField(
            model_name='contentcreater',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='contentcreater',
            name='profilePicture',
        ),
        migrations.RemoveField(
            model_name='contentcreater',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='stafftable',
            name='location',
        ),
        migrations.RemoveField(
            model_name='stafftable',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='stafftable',
            name='roles',
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account', models.CharField(choices=[('Yes', 'Create an Account'), ('No', 'Do Not Create an Account')], max_length=20, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userInfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.nitacagrausers')),
            ],
        ),
        migrations.AddField(
            model_name='contentcreater',
            name='userInfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userinformation', to='Accounts.nitacagrausers'),
        ),
        migrations.AddField(
            model_name='stafftable',
            name='userInfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.nitacagrausers'),
        ),
    ]