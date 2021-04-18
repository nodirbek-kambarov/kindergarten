from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import first_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
    path('news/', include('news.urls', namespace='news')),
    path('about/', include('workers.urls', namespace='about')),
    path('contact/', include('crm.urls', namespace='contact')),
    path('gallery/', include('gallery.urls', namespace='gallery')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
