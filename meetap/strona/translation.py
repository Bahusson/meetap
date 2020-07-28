from modeltranslation.translator import translator, TranslationOptions
from strona.models import Pageitem, Blog


class PageitemsTranslate(TranslationOptions):
    fields = '__all__'


translator.register(Pageitem, PageitemsTranslate)


class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body', 'image', 'video')


translator.register(Blog, BlogsTranslate)
