# Generated by Django 4.2.2 on 2023-06-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0012_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='size',
            field=models.CharField(blank=True, choices=[('APPLIED', 'Applied'), ('BACKLOG', 'Backlog'), ('DENIED', 'Denied'), ('INTERVIEW', 'Interview')], max_length=100, null=True),
        ),
    ]
