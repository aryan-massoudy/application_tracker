# tracker/admin.py
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'user', 'application_date', 'status')
    list_filter = ('status', 'user')
    search_fields = ('company_name', 'position', 'user__username')