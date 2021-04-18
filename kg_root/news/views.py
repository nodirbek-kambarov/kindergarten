from django.shortcuts import render, get_object_or_404
from news.models import News
from django.views.generic import ListView


class NewsPage(ListView):
    template_name = 'news.html'
    model = News
    paginate_by = 2


def get_news(request, pk):

    news = get_object_or_404(News, pk=pk)
    return render(request, './get_news.html', {'news': news})
