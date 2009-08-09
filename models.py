from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
try:
    from markdown import markdown
except ImportError:
    class MarkdownNotFound(Exception):
        def __str__(self):
            return "Markdown is not installed!"
    raise MarkdownNotFound
from prana.languages import LANGUAGES

class Word(models.Model):
    """
    Word/Meaning class
    """
    word = models.CharField(_("word"), max_length=80)
    meaning = models.CharField(_("meaning"), max_length=100)
    language = models.CharField(_("language"), max_length=2, choices=LANGUAGES, default='en')
    comment = models.TextField(_("comment"),  blank=True, help_text=_("Use Markdown sintax to add a comment to the word"))
    html_comment = models.TextField(editable=False, blank=True)
    date = models.DateTimeField(_("date"), editable=False, default=datetime.now)

    class Meta:
        ordering = ("-date",)
        verbose_name = _("word")
        verbose_name_plural = _("words")

    def __unicode__(self):
        return "%s (%s)" % (self.word, self.get_language_display())

    def save(self):
        self.html_comment = markdown(self.comment)
        super(Word, self).save()

    @permalink
    def get_absolute_url(self):
        pass

class Verb(models.Model):
    """
    Verb class
    """
    verb = models.CharField(_("verb"), max_length=80, help_text=_("Use here the infinitive tense, e.g.: To be"))
    meaning = models.CharField(_("meaning"), max_length=80, help_text=_("The infinitive tense in your language, e.g.: Ser o estar"))
    language = models.CharField(_("language"), max_length=2, choices=LANGUAGES, default='en')
    content = models.TextField(_("content"), blank=True, \
        help_text=_("e.g.: I am [2x Space + Intro] You are [2x Space + Intro] He is... and so forth. Use Markdown sintax here."))
    html_content = models.TextField(editable=False, blank=True)
    comment = models.TextField(_("comment"),  blank=True, help_text=_("Use Markdown sintax to add a comment to the word"))
    html_comment = models.TextField(editable=False, blank=True)
    date = models.DateTimeField(_("date"), editable=False, default=datetime.now)

    class Meta:
        ordering = ("-date",)
        verbose_name = _("verb")
        verbose_name_plural = _("verbs")

    def __unicode__(self):
        return "%s (%s)" % (self.verb, self.get_language_display())

    def save(self):
        self.html_content = markdown(self.content)
        self.html_comment = markdown(self.comment)
        super(Verb, self).save()

    @permalink
    def get_absolute_url(self):
        pass

