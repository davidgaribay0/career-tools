# Generated by Django 4.2.2 on 2023-06-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0004_jobapplication_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website_url',
            field=models.URLField(blank=True),
        ),
    ]
