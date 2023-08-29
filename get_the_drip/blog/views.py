from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def show_about(request: HttpRequest):
    return HttpResponse("<h1>This is mazafaka coolest drip blog in MISIS &gt:(</h1>")


def main_page_redirect(request: HttpRequest):
    return redirect("about", permanent=True)
