# Generated by Django 4.2.2 on 2023-06-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt', '0005_alter_company_description_alter_company_website_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='remote',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]