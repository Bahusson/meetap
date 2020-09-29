from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from .models import (
 PageSkin as S, Blog as B,  PageNames as P, RegNames, ProfileNames)
from .forms import ProfileForm
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (
 PageElement as pe, PageLoad, ActivePageItems)
import pytz
import datetime
from django.views import View


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


# Wszystkie aktualności.
def allblogs(request):
    # pe_b = pe(B)
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    context = {
     'blogs': active_blogs, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allblogs.html'
    return render(request, template, context_lazy)


# Pojedyńcze aktualności w zbliżeniu.
def blog(request, blog_id):
    pe_b = pe(B)
    pe_b_id = pe_b.by_id(
     G404=G404, id=blog_id)
    context = {
     'blog': pe_b_id, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/blog.html'
    return render(request, template, context_lazy)


# Login Required
# Strona ustawień profilu  widok oparty na klasiee :D.
class Myprofile(View):
    formclass = ProfileForm
    template = 'forms/myprofile.html'
    regitem = pe(RegNames).baseattrs
    profileitem = pe(ProfileNames).baseattrs

    # Specjalna funkcja zastępująca __init_ ,
    # któremu nie można przesłać parametru request.
    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        self.userdata = User.objects.get(
         mnemo_login=request.user.mnemo_login)
        self.context = {
         'udata': self.userdata,
         'regitem': self.regitem,
         'profileitem': self.profileitem,
              }
        # call the view
        return super(Myprofile, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.formclass(
         request.POST, request.FILES, instance=self.userdata)
        if form.is_valid():
            form.save()
            return redirect('myprofile')

    def get(self, request, *args, **kwargs):
        form = self.formclass(instance=self.userdata)
        pl = PageLoad(P, L)
        new_context = {"form": form, }
        self.context.update(new_context)
        context_lazy = pl.lazy_context(skins=S, context=self.context)
        return render(request, self.template, context_lazy)


# Usuwacz profilu
def myprofiledelete(request):
    userdata = User.objects.get(
     mnemo_login=request.user.mnemo_login)
    if request.method == 'POST':
        userdata.delete()
        return redirect('home')
    else:
        form = ProfileForm(instance=userdata)
        regitem = pe(RegNames).baseattrs
        profileitem = pe(ProfileNames).baseattrs
        context = {
         'udata': userdata,
         'form': form,
         'regitem': regitem,
         'profileitem': profileitem,
         }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/myprofiledelete.html'
        return render(request, template, context_lazy)
