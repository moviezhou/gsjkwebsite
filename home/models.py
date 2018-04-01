from __future__ import absolute_import, unicode_literals

from django.db import models

from news.models import *

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    class Meta:
        verbose_name = "首页"
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
        # news_entries = self.get_children().get(slug='news').get_children().get(slug='highlights').get_children().specific()
        news_entries = NewsPage.objects.descendant_of(self.get_children().get(slug='news').get_children().get(slug='highlights')).live().order_by('-date') #ColumnPage.objects.filter(slug="highlights").specific()
        news_latest = NewsPage.objects.descendant_of(self.get_children().get(slug='news').get_children().get(slug='latest')).live().order_by('-date')
        news_industry = NewsPage.objects.descendant_of(self.get_children().get(slug='news').get_children().get(slug='industry')).live().order_by('-date')
        news_policy = NewsPage.objects.descendant_of(self.get_children().get(slug='news').get_children().get(slug='policy')).live().order_by('-date')
        partybuilding_news_entries = NewsPage.objects.descendant_of(self.get_children().get(slug='partybuilding').get_children().get(slug='dynamic')).live().order_by('-date')
        context['news_entries'] = news_entries
        context['news_latest'] = news_latest
        context['news_industry'] = news_industry
        context['news_policy'] = news_policy
        context['partybuilding_news_entries'] = partybuilding_news_entries
        return context