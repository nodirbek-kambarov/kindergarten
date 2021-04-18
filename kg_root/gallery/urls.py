from django.urls import path


from gallery.views import gallery_page

app_name = 'categories'

urlpatterns = [
    path('', gallery_page, name='gallery'),
    ]
