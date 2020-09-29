from django.urls import path
from . import views
from.views import Myprofile

urlpatterns = [
    path('', views.home, name='home'),
    path('aktualnosci', views.allblogs, name='allblogs'),
    path('aktualnosc/<int:blog_id>/', views.blog, name='blog'),
    path('myprofile', Myprofile.as_view(), name='myprofile'),
    path('myprofiledelete', views.myprofiledelete, name='myprofiledelete'),
]
