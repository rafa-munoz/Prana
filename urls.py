from django.conf.urls.defaults import *
from prana.models import Verb, Word
from prana.views import index, random, random_lang, detail

urlpatterns = patterns('',
    url(r'^$', index, name='prana-index'),
    url(r'^(?P<lang>[a-z]{2})/$', index, name='prana-index-lang'),
    url(r'^word/(?P<object_id>\d+)/$', detail, {'type': 'word'}, name='prana-worddetail'),
    url(r'^verb/(?P<object_id>\d+)/$', detail, {'type': 'verb'}, name='prana-verbdetail'),
    url(r'^random/$', random, name='prana-random'),
    url(r'^random/(?P<w_or_v>[0-1]{1})/$', random, name='prana-random-worv'),
    url(r'^random/(?P<lang>[a-z]{2})/$', random_lang, name='prana-random-lang'),
    url(r'^random/(?P<lang>[a-z]{2})/(?P<w_or_v>[0-1]{1})/$', random_lang, name='prana-random-lang-worv'),
)

