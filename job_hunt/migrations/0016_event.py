# Generated by Django 4.2.2 on 2023-06-13 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0015_remove_jobapplication_application_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(choices=[('PHONE_CALL', 'Phone Call'), ('INTERVIEW', 'Interview'), ('EMAIL', 'Email')], max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('notes', models.TextField(blank=True)),
                ('next_steps', models.TextField(blank=True)),
                ('attendants', models.ManyToManyField(related_name='events', to='job_hunt.profile')),
                ('job_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='job_hunt.jobapplication')),
            ],
        ),
    ]