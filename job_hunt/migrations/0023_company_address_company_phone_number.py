# Generated by Django 4.2.2 on 2023-06-15 23:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0022_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='US'),
        ),
    ]
