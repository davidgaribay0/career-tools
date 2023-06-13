# Generated by Django 4.2.2 on 2023-06-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0016_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('PHONE_CALL', 'Phone Call'), ('INTERVIEW', 'Interview'), ('EMAIL', 'Email')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='attendants',
            field=models.ManyToManyField(blank=True, related_name='events', to='job_hunt.profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]