from django.urls import path

from . import views

urlpatterns = [
    path('events_panel', views.events_panel, name='events_panel'),
    path('events', views.events, name="events"),
    path(
     'event<int:event_id>/<show_divisions>/<show_taxes>',
     views.event, name="event"),
    path('make_event', views.make_event, name='make_event'),
    # path('edit_event<int:event_id>', views.edit_event, name='edit_event'),
]
