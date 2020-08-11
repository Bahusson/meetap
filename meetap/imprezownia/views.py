from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from strona.models import PageNames as P, PageSkin as S
from .models import (EventsMenuNames as EMN)
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
