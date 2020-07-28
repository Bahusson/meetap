from modeltranslation.translator import translator, TranslationOptions
from strona.models import Pageitem, Blog
from meetap.core.snippets import all_names


class PageitemsTranslate(TranslationOptions):
    allfields = all_names(Pageitem)
    fields = allfields


translator.register(Pageitem, PageitemsTranslate)


class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body', 'image', 'video')


translator.register(Blog, BlogsTranslate)
