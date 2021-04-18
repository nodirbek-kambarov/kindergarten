from django.urls import path

from news.views import NewsPage, get_news

app_name = 'news'

urlpatterns = [
    path('', NewsPage.as_view(), name='news'),
    path('get/<int:pk>', get_news, name='get'),
]
