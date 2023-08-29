from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

menu = ['Новости', 'Подборки', 'О нас']


def about_page(request: HttpRequest):
    return render(request, "blog/about.html", context={
        'title': "About DRIP",
        'menu': menu
    })


def main_page(request: HttpRequest):
    return render(request, "blog/index.html", context={
        'title': "Get the DRIP",
        'menu': menu
    })


def main_page_redirect(request: HttpRequest):
    return redirect('main', permanent=True)
