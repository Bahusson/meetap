from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from strona.models import PageNames as P, PageSkin as S
from .models import (EventsMenuNames as EMN, Event as E)
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (
 PageElement as pe, PortalLoad, ActivePageItems)
import pytz
import datetime


# Panel Wydarzeń
def events_panel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/eventspanel.html'
    return render(request, template, context_lazy)


def my_events(request):
    page_event = pe(E)
    pe_elements = page_event.elements
    context = {
     'events': pe_elements, }
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'imprezownia/myevents.html'
    return render(request, template, context_lazy)


def event(request, event_id):
    pe_b = pe(E)
    pe_b_id = pe_b.by_id(
     G404=G404, id=event_id)
    context = {
     'event': pe_b_id, }
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(skins=S)
    template = 'imprezownia/event.html'
    return render(request, template, context_lazy)
