from django.contrib import admin
from .models import Workers

@admin.register(Workers)
class WorkersModelAdmin(admin.ModelAdmin):
    list_display = ['workers_name']
    search_fields = ['workers_name']



