from django.template import Library
from prana.languages import LANGUAGES

register = Library()

@register.simple_tag
def lang_name(lang):
    """
    Prints language name and it's initials.
    {% lang [lang_initials] %}
    """
    for l in LANGUAGES:
        if lang == l[0]:
            return "%s (%s)" % (l[0], l[1])
