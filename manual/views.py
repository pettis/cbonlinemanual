from .models import ManualPage
from django.shortcuts import render
from django.http import Http404


def index(request):
    navigation = ManualPage.objects.filter(published=True, parent=None)
    return render(request, 'view_page.html', {'navigation': navigation})


def view_page(request, slug):
    navigation = ManualPage.objects.filter(published=True, parent=None)
    try:
        page = ManualPage.objects.get(slug=slug, published=True)
    except ManualPage.DoesNotExist:
        raise Http404
    return render(request, 'view_page.html', {'navigation': navigation,
                                              'page': page})