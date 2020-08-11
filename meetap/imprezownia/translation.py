from modeltranslation.translator import translator, TranslationOptions
from imprezownia.models import EventsMenuNames
from meetap.core.snippets import all_names


class EventsMenuNamesTranslate(TranslationOptions):
    allfields = all_names(EventsMenuNames)
    fields = allfields


translator.register(EventsMenuNames, EventsMenuNamesTranslate)
