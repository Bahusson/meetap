from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from strona.models import (PageNames as P, PageSkin as S, P_S_A as PSA)
from .models import (
 EventsMenuNames as EMN, Event as E, PartyDivider as PD, UserRole as UR,
 TaxPanel as TP, Tax)
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (PageElement as pe, PortalLoad)
from meetap.core.snippets import booleanate as bot, flare
from .forms import EventForm, PartyDividerForm, TaxPanelForm


# Panel Wydarzeń (pusty widok z panelem bocznym)
def events_panel(request):
    # zdefiniuj dodatkowe konteksty tutaj.
    pl = PortalLoad(P, L, EMN, PSA)
    context_lazy = pl.lazy_context(skins=S)
    template = 'panels/eventspanel.html'
    return render(request, template, context_lazy)


# Zbiorczy widok wydarzeń użytkownika.
def events(request):
    userdata = User.objects.get(
     mnemo_login=request.user.mnemo_login)
    # Widzi tylko własne wpisy
    efilter = E.objects.filter(owner=userdata)
    context = {
     'events': efilter, }
    pl = PortalLoad(P, L, EMN, PSA)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'imprezownia/user_events.html'
    return render(request, template, context_lazy)


# Widok edycji wydarzenia dla twórcy.
def event(request, event_id, show_divisions, show_taxes):
    # Tutaj przetestuj, czy możesz
    editor_view = True  # Ten formularz pozwala na edycję wydarzenia
    pe_e = pe(E)
    pe_e_id = pe_e.by_id(G404=G404, id=event_id)
    userdata = User.objects.get(
     mnemo_login=request.user.mnemo_login)
    user_id = userdata.mnemo_login
    #flare(user_id)
    owner_id = pe_e_id.owner.mnemo_login
    #flare(owner_id)
    if user_id == owner_id:
        flare("True_af")
        pass
    else:
        flare("False_af")
        return redirect('logger')
    pe_pd = PD.objects.filter(from_event=event_id)
    pe_ur = UR.objects.filter(from_event__from_event=event_id)
    pe_tp = TP.objects.filter(from_event=event_id)
    pe_tax = Tax.objects.filter(from_event__from_event=event_id)
    baseform = EventForm(instance=pe_e_id)
    formdict = {
        "True": PartyDividerForm,
        "False": TaxPanelForm,
    }
    deletiondict = {
        "True": PD,
        "False": TP,
    }
    if 'make_event_child' in request.POST:
        form = formdict[show_divisions](request.POST, request.FILES)
        if form.is_valid():
            form.save(pe_e_id)
            return redirect(request.META.get('HTTP_REFERER'))
    if "delete_event" in request.POST:
        pe_e_id.delete()
        return redirect('events')
    if "delete_division" in request.POST:
        div_value = request.POST['delete_division']
        div_for_deletion = pe(deletiondict[show_divisions]).by_id(
         G404=G404, id=div_value)
        div_for_deletion.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    if "update_event" in request.POST:
        baseform = EventForm(request.POST, request.FILES, instance=pe_e_id)
        if baseform.is_valid():
            baseform.save(userdata)
            return redirect(request.META.get('HTTP_REFERER'))

    sh_dv = bot(show_divisions)
    sh_tx = bot(show_taxes)
    form = formdict[show_divisions]
    context = {'event': pe_e_id,
               'dividers': pe_pd,
               'userroles': pe_ur,
               'tax_panels': pe_tp,
               'taxes': pe_tax,
               'show_divisions': sh_dv,
               'show_taxes': sh_tx,
               "form": form,
               "baseform": baseform,
               "editor_view": editor_view,
               }
    pl = PortalLoad(P, L, EMN, PSA)
    context_lazy = pl.lazy_context(skins=S, context=context)
    template = 'imprezownia/eventpage.html'
    return render(request, template, context_lazy)


# Dodaj nowe wydarzenie.
def make_event(request):
    userdata = User.objects.get(
     mnemo_login=request.user.mnemo_login)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(userdata)
            return redirect('events')
    else:
        form = EventForm()
        context = {
         "form": form,
        }
        pl = PortalLoad(P, L, EMN, PSA)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'imprezownia/make_event.html'
        return render(request, template, context_lazy)


# Edytuj dział wydarzenia.
def edit_divider(request):
    editor_view = True  # Ten formularz pozwala na edycję wydarzenia
    userdata = User.objects.get(
     mnemo_login=request.user.mnemo_login)
