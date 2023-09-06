from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='main'),
    path('about/', views.About.as_view(), name='about'),
    path('addpub/', views.AddPublication.as_view(), name='add_pub'),
    path('feedback/', views.feedback_page, name='feedback'),
    path('login/', views.login_page, name='login'),
    path('publication/<slug:pub_slug>', views.ShowPublication.as_view(), name='publication'),
    path('category/<slug:cat_slug>', views.PublicationCategory.as_view(), name='category'),
    path('register/', views.Register.as_view(), name='register')
]
