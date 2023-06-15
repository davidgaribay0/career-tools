from django.contrib import admin
from django.forms import Textarea
from .models import JobApplication, Company, Attachment, Profile, Event
from django.db import models


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

class EventInline(admin.StackedInline):
    model = Event
    extra = 1

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_filter = ['status']
    inlines = [AttachmentInline, EventInline]
    list_display = ('title', 'company', 'status', 'date_applied','get_events' )

    def get_events(self, obj):
        return len([event.event_name for event in obj.events.all()])

    get_events.short_description = 'Events'



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass