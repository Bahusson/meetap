from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import FormItems
from meetap.core.snippets import all_names


class FormItemsTranslate(TranslationOptions):
    allfields = all_names(FormItems)
    fields = allfields


translator.register(FormItems, FormItemsTranslate)
