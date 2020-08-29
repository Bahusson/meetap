from modeltranslation.translator import translator, TranslationOptions
from imprezownia.models import (
 EventsMenuNames, Event, PartyDivider, UserRole, TaxPanel, Tax)
from meetap.core.snippets import all_names


class EventsMenuNamesTranslate(TranslationOptions):
    allfields = all_names(EventsMenuNames)
    fields = allfields


translator.register(EventsMenuNames, EventsMenuNamesTranslate)


class EventTranslate(TranslationOptions):
    fields = ("title", "body", "other_preferences", "other_drugs")


translator.register(Event, EventTranslate)


class PartyDividerTranslate(TranslationOptions):
    fields = ("title", "descr")


translator.register(PartyDivider, PartyDividerTranslate)


class UserRoleTranslate(TranslationOptions):
    fields = ("title", "role_descr")


translator.register(UserRole, UserRoleTranslate)


class TaxPanelTranslate(TranslationOptions):
    fields = ("title", "descr")


translator.register(TaxPanel, TaxPanelTranslate)


class TaxTranslate(TranslationOptions):
    fields = ("title", "descr")


translator.register(Tax, TaxTranslate)
