from django.contrib import admin

# Register your models here.
from .models import (
 EventsMenuNames, Event, PartyDivider, UserRole, TaxPanel, Tax)


admin.site.register(EventsMenuNames)
admin.site.register(Event)
admin.site.register(PartyDivider)
admin.site.register(UserRole)
admin.site.register(TaxPanel)
admin.site.register(Tax)
