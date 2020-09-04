from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from strona.models import PageNames as P, PageSkin as S
from .models import (
 EventsMenuNames as EMN, Event as E, PartyDivider as PD, UserRole as UR,
 TaxPanel as TP, Tax)
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (
 PageElement as pe, PortalLoad, ActivePageItems)
from meetap.core.snippets import booleanate as bot
import pytz
import datetime


# Panel Wydarzeń
def events_panel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/eventspanel.html'
    return render(request, template, context_lazy)


def events(request):
    userdata = User.objects.get(
     id=request.user.id)
    # Widzi tylko własne wpisy
    efilter = E.objects.filter(owner=userdata)
    context = {
     'events': efilter, }
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'imprezownia/user_events.html'
    return render(request, template, context_lazy)


def event(request, event_id, show_divisions, show_taxes):
    pe_e = pe(E)
    pe_e_id = pe_e.by_id(G404=G404, id=event_id)
    pe_pd = PD.objects.filter(from_event=event_id)
    pe_ur = UR.objects.filter(from_event__from_event=event_id)
    pe_tp = TP.objects.filter(from_event=event_id)
    pe_tax = Tax.objects.filter(from_event__from_event=event_id)
    sh_dv = bot(show_divisions)
    sh_tx = bot(show_taxes)

    context = {'event': pe_e_id,
               'dividers': pe_pd,
               'userroles': pe_ur,
               'tax_panels': pe_tp,
               'taxes': pe_tax,
               'show_divisions': sh_dv,
               'show_taxes': sh_tx,
               }
    print(context)
    pl = PortalLoad(P, L, EMN)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'imprezownia/eventpage.html'
    return render(request, template, context_lazy)
