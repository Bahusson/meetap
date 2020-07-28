from django.contrib import admin


# Register your models here.
from .models import Pageitem, Blog, PageSkin, FormElement


admin.site.register(Pageitem)
admin.site.register(Blog)
admin.site.register(PageSkin)
admin.site.register(FormElement)
