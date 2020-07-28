from modeltranslation.translator import translator, TranslationOptions
from rekruter.models import FormItems


class FormItemsTranslate(TranslationOptions):
    fields = '__all__'


translator.register(FormItems, FormItemsTranslate)
