from django.contrib import admin
from django.forms import Textarea
from .models import JobApplication, Company, Attachment, Profile
from django.db import models


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_filter = ['status']
    inlines = [AttachmentInline]
    list_display = ('title', 'company', 'status', 'date_applied')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass