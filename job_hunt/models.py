from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    STATUS = (
        ('APPLIED', 'Applied'),
        ('BACKLOG', 'Backlog'),
        ('DENIED', 'Denied'),
        ('INTERVIEW', 'Interview'),
        ('OFFER_RECIEVED', 'Offer recieved'),
        ('OFFER_REJECTED', 'Offer rejected'),
        ('OFFER_ACCEPTED', 'Offer accepted'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    url=models.URLField(blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)
    notes=models.TextField(blank=True)
    remote = models.BooleanField(blank=True, default=False, null=True)
    date_applied = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.title


class Attachment(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='attachments', null=True)
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return self.file.name
    

class Profile(models.Model):
    full_name = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url =models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='attachments/', blank=True)
    cover_letter = models.FileField(upload_to='attachments/', blank=True)
    email = models.EmailField(blank=True, null=True)
        
    def __str__(self):
        return self.full_name