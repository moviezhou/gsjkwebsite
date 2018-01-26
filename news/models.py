from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# from wagtail.wagtailcore.fields import StreamField
# from wagtail.wagtailcore import blocks
# from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.wagtailimages.blocks import ImageChooserBlock

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
        column_entries = self.get_children()
        context['column_entries'] = column_entries
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

    def get_context(self, request):
        context = super(BusinessIndexPage, self).get_context(request)
        column_entries = self.get_children()
        context['column_entries'] = column_entries
        return context

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

    def get_context(self, request):
        context = super(ColumnPage, self).get_context(request)
        if request.path == '/business/domain' or request.path == '/business/investment':
            column_entries = self.get_children()
            context['column_entries'] = column_entries
        return context

    
    def serve(self, request):
        if request.path == '/business/domain':
            return render(request, 'news/business_domain.html', self.get_context(request))
        elif request.path == '/business/investment':
            return render(request, 'news/enterprise_page.html', self.get_context(request))
        else:
            return render(request, 'news/column_page.html', self.get_context(request))
    

class NewsPage(Page):
    class Meta:
        verbose_name = "新闻"
    date = models.DateField(verbose_name="日期")
    intro = models.CharField(max_length=250, verbose_name="简介")
    body = RichTextField(blank=True, verbose_name="内容")
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="缩略图"
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

class EnterprisePage(Page):
    class Meta:
        verbose_name = "企业"

    ENTERPRISE_CATEGORY = (
        ("全资企业", "全资企业"),
        ("控股企业", "控股企业"),
        ("参股企业", "参股企业"),)

    
    enterprise_category = models.CharField(max_length=10, choices=ENTERPRISE_CATEGORY, default=1, verbose_name="公司类型")   
    enterprise_name = models.CharField(max_length=60, verbose_name="公司名称")
    enterprise_intro = RichTextField(blank=True, verbose_name="公司简介")
    enterprise_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logo"
    )
    enterprise_website = models.CharField(blank=True, max_length=200, verbose_name="网址")

    content_panels = Page.content_panels + [
        FieldPanel('enterprise_category'),
        FieldPanel('enterprise_name'),
        FieldPanel('enterprise_intro'),
        ImageChooserPanel('enterprise_logo'),
        FieldPanel('enterprise_website'),
    ]

    def get_context(self, request):
        context = super(EnterprisePage, self).get_context(request)
        column_entries = self.get_children()
        print(column_entries)
        context['column_entries'] = column_entries
        return context

class BusinessDomain(Page):
    class Meta:
        verbose_name = "业务领域"

    BUSINESS_CATEGORY = (
        ("主金融", "主金融"),
        ("类金融", "类金融"),
        ("平台类", "平台类"),
        ("其他类", "其他类"),)

    business_category = models.CharField(max_length=10, choices=BUSINESS_CATEGORY, default=1, verbose_name="业务领域")   
    
    business_name = models.CharField(max_length=60, verbose_name="业务名称")
    business_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="业务领域图标")
    
    # business_intro = StreamField([
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),])

    business_intro = RichTextField(blank=True, verbose_name="领域简介")

    content_panels = Page.content_panels + [
        FieldPanel('business_category'),
        FieldPanel('business_name'),
        ImageChooserPanel('business_icon'),
        FieldPanel('business_intro'),]