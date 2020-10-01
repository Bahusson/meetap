from modeltranslation.translator import translator, TranslationOptions
from strona.models import (
 PageNames, Blog, BlogNames, RegNames, ProfileNames, P_S_A,)
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


class ProfileNamesTranslate(TranslationOptions):
    allfields = all_names(ProfileNames)
    fields = allfields


translator.register(ProfileNames, ProfileNamesTranslate)


class P_S_ATranslate(TranslationOptions):
    fields = ("title", "link_external", "image", "body",)


translator.register(P_S_A, P_S_ATranslate)
