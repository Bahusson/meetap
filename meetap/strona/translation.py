from modeltranslation.translator import translator, TranslationOptions
from strona.models import PageNames, Blog, BlogNames, RegNames
from meetap.core.snippets import all_names


class PageNamesTranslate(TranslationOptions):
    allfields = all_names(PageNames)
    fields = allfields


translator.register(PageNames, PageNamesTranslate)


class BlogsTranslate(TranslationOptions):
    fields = ('title', 'body', 'image', 'video')


translator.register(Blog, BlogsTranslate)


class BlogNamesTranslate(TranslationOptions):
    allfields = all_names(BlogNames)
    fields = allfields


translator.register(BlogNames, BlogNamesTranslate)


class RegNamesTranslate(TranslationOptions):
    allfields = all_names(RegNames)
    fields = allfields


translator.register(RegNames, RegNamesTranslate)
