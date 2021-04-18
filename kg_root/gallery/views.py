from django.shortcuts import render
from gallery.models import Gallery


def gallery_page(request):
    gallery_list = Gallery.objects.all()

    return render(request, './gallery.html', {'gallery_list': gallery_list})
