from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class CompanyIndexPage(Page):
    class Meta:
        verbose_name = "走进金控二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(CompanyIndexPage, self).get_context(request)
        column_entries = self.get_children() # .get(slug='intro').get_children().specific()
        for i in column_entries:
            print(i.get_children().specific())
        context['column_entries'] = column_entries
        # print(column_entries)
        return context

class NewsIndexPage(Page):
    class Meta:
        verbose_name = "资讯中心二级页面"

    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BusinessIndexPage(Page):
    class Meta:
        verbose_name = "集团业务二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class PartyBuildingIndexPage(Page):
    class Meta:
        verbose_name = "党建工作二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class EnterpriseCultureIndexPage(Page):
    class Meta:
        verbose_name = "企业文化二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class AcademyIndexPage(Page):
    class Meta:
        verbose_name = "金控学院二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ContactUsIndexPage(Page):
    class Meta:
        verbose_name = "联系我们二级页面"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ColumnPage(Page):
    class Meta:
        verbose_name = "专栏"
    intro = RichTextField(blank=True)

    # def get_context(self, request):
    #     context = super(ColumnPage, self).get_context(request)
    #     # news_items = ColumnPage.objects.live().order_by('-first_published_at')
    #     news_items = self.get_children().live().order_by('-date')


    #     print(news_items)

    #     return context

    
    def serve(self, request):
        return render(request, 'news/column_page.html', self.get_context(request))
    

class NewsPage(Page):
    class Meta:
        verbose_name = "新闻"
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    promote_panels = Page.promote_panels + [
        ImageChooserPanel('representative_image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]