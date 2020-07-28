from django.shortcuts import (render, get_object_or_404 as G404)
# from rekruter.models import User
from .models import (PageSkin as S, Blog as B)
from strona.models import Pageitem as P
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (PageElement as pe, PageLoad, ActivePageItems)
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    context = {
     'blogs': active_blogs,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)
