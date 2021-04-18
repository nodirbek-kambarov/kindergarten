from django.contrib import admin
from .models import News




@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_date']
    search_fields = ['news_title']


