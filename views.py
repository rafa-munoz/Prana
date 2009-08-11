import random as random_module
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list_detail import object_detail
from django.utils.translation import ugettext_lazy as _
from prana.templatetags.prana_tags import lang_name
from prana.models import Word, Verb

def _url_params(querydict):
    """
    Returns all request GET params.
    """
    params = querydict.lists()
    if not params:
        return ""
    else:
        url = "?"
        i = 0
        for p in params:
            if i > 0:
                url += "&"
            url += "%s=%s" % (p[0], p[1][0])
            i += 1

        return url

def index(request, lang=None):
    """
    Index page. Lists all words and verbs.
    Language filters are available.
    """
    qs_words = Word.objects.all()
    qs_verbs = Verb.objects.all()

    # It may be rewritten better
    word_langs = qs_words.distinct()
    verb_langs = qs_verbs.distinct()
    w_langs = [l.language for l in word_langs]
    v_langs = [l.language for l in verb_langs]
    aux = w_langs + v_langs
    langs = set(aux)

    if lang != None:
        qs_words = qs_words.filter(language=lang)
        qs_verbs = qs_verbs.filter(language=lang)

    dictionary = {
        "words": qs_words,
        "verbs": qs_verbs,
        "w_langs": w_langs,
        "v_langs": v_langs,
        "langs": langs,
        "request_get": _url_params(request.GET),
    }

    if lang != None:
        dictionary["title"] = _("Filter by: %s") % lang_name(lang)

    return render_to_response("prana/index.html", dictionary,
        context_instance=RequestContext(request))

def detail(request, object_id, type):
    """
    Details of a word/verb.
    """
    if type == "word":
        queryset = Word.objects.all()
    elif type == "verb":
        queryset = Verb.objects.all()

    return object_detail(request, queryset=queryset, object_id=object_id,
        extra_context={"request_get": _url_params(request.GET)})

def random(request, w_or_v=None):
    """
    Random page for either words or verbs.
    """
    template = "prana/%s_detail.html"

    # Random choosing between word or verbs
    if w_or_v == None:
        r1 = random_module.randint(1, 2)
    else:
        r1 = int(w_or_v) + 1

    if r1 == 1: # Word
        template = template % "word"
        count = Word.objects.count()
    elif r1 == 2: # Verb
        template = template % "verb"
        count = Verb.objects.count()

    # No objects in DB yet
    if count == 0:
        return # TODO error page

    # Choosing a random object
    found = False
    while found == False:
        r2 = random_module.randint(1, count)
        try:
            if r1 == 1:
                o = Word.objects.get(pk=r2)
            elif r1 == 2:
                o = Verb.objects.get(pk=r2)
            found = True
        except ObjectDoesNotExist:
            pass

    dictionary = {
        "object": o,
        "request_get": _url_params(request.GET),
    }

    return render_to_response(template, dictionary, context_instance=RequestContext(request))

def random_lang(request, lang, w_or_v=None):
    """
    Random page for a given lang.
    Filter by word or verb (w_or_b) is available.
    Use w_or_b=0 for only words or 1 for only verbs
    """
    template = "prana/%s_detail.html"

    if w_or_v == None:
        r = random_module.randint(1, 2)

        qm = Word.objects if (r == 1) else Verb.objects
        # If number of words is 0 go for verbs and viceversa
        r = (r % 2 + 1) if (qm.filter(language=lang).count() == 0) else r

        if r == 1: # Word
            qm = Word.objects
            template = template % "word"

        elif r == 2: # Verb
            qm = Verb.objects
            template = template % "verb"

        qs = qm.filter(language=lang)
        pks = [object.pk for object in qs]
        pk = random_module.choice(pks)
        o = qm.get(pk=pk)

    else:
        if w_or_v == "0":
            qm = Word.objects
            template = template % "word"
        else:
            qm = Verb.objects
            template = template % "verb"
        qs = qm.filter(language=lang)
        pks = [object.pk for object in qs]
        pk = random_module.choice(pks)
        o = qm.get(pk=pk)

    dictionary = {
        "object": o,
        "request_get": _url_params(request.GET),
    }

    return render_to_response(template, dictionary, context_instance=RequestContext(request))

