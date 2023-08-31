from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('about/', views.about_page, name='about'),
    path('addpub/', views.add_pub_page, name='add_pub'),
    path('feedback/', views.feedback_page, name='feedback'),
    path('login/', views.login_page, name='login'),
    path('publication/<int:pub_id>', views.show_publication, name='show_pub')
]
