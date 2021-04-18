from django.shortcuts import render

from workers.models import Workers


def about_page(request):
    workers_list = Workers.objects.all()

    return render(request, './about.html', {'workers_list': workers_list})
