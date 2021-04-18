from django.urls import path

from crm.views import contact_page

app_name = 'categories'

urlpatterns = [
    path('', contact_page, name='contact'),
    ]
