from __future__ import absolute_import, unicode_literals

from django.db import models

from news.models import NewsPage

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    promote_panels = [
        ImageChooserPanel('banner_image'),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        news_entries = self.get_children().get(slug='news').get_children().get(slug='highlights').get_children().specific()
        news_latest = self.get_children().get(slug='news').get_children().get(slug='latest').get_children().specific()
        partybuilding_news_entries = self.get_children().get(slug='partybuilding').get_children().get(slug='dynamic').get_children().specific()
        context['news_entries'] = news_entries
        context['news_latest'] = news_latest
        context['partybuilding_news_entries'] = partybuilding_news_entries
        return context