from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Publication

header_links = [
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Add publication', 'url_name': 'add_pub'},
    {'title': 'Feedback', 'url_name': 'feedback'}
]

categories = ['Street style', 'Classic', 'Urban bitch', 'Gay hunter']


def about_page(request: HttpRequest):
    return render(request, "blog/about.html", context={
        'title': "About DRIP",
        'header_links': header_links
    })


def main_page(request: HttpRequest):
    publications = Publication.objects.all()
    return render(request, "blog/index.html", context={
        'title': "Get the DRIP",
        'categories': categories,
        'publications': publications,
        'header_links': header_links
    })


def feedback_page(request: HttpRequest):
    return HttpResponse("Come on, bitch, say it right to my face!")


def add_pub_page(request: HttpRequest):
    return HttpResponse("What do you want to add, stupid cunt?")


def login_page(request: HttpRequest):
    return HttpResponse("Who fuck are you?")


def show_publication(request: HttpRequest, pub_id: int):
    return HttpResponse(f"Article with id = {pub_id}")
