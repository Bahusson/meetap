from django.urls import path

from . import views

urlpatterns = [
    path('events_panel', views.events_panel, name='events_panel'),
    # path('add_new_event', views.add_new_event, name='add_new_event'),
    # path('edit_my_event', views.edit_my_event, name='edit_my_event'),
]
