from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('aktualnosci', views.allblogs, name='allblogs'),
    path('aktualnosc/<int:blog_id>/', views.blog, name='blog'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('myprofiledelete', views.myprofiledelete, name='myprofiledelete'),
]
