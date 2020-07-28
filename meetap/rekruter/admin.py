from django.contrib import admin

# Register your models here.
from .models import FormItems, User

admin.site.register(FormItems)
admin.site.register(User)
