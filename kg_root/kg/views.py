from django.shortcuts import render
from carousel.models import Carousel
from news.models import News
from workers.models import Workers


def first_page(request):
    slider_list = Carousel.objects.all()
    workers_list = Workers.objects.all()
    news_list = News.objects.all()[:6]
    context = {'slider_list': slider_list, 'workers_list': workers_list, 'news_list': news_list}

    return render(request, './index.html', context
                  )
