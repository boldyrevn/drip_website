from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_redirect),
    path('about/', views.show_about, name='about')
]
