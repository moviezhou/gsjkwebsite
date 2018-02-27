from django.db import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
    )
from wagtail.wagtailforms.models import AbstractForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from django.contrib import messages
# from wagtail.wagtailcore.fields import StreamField
# from wagtail.wagtailcore import blocks
# from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class CompanyIndexPage(Page):
    class Meta:
        verbose_name = "走进金控二级页面"
    
    subpage_types = ['ColumnPage']
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
        
    subpage_types = ['ColumnPage']
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # Ordering news by publish date only when news_index_page rendered
    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        if len(self.get_children()) > 0:
            first_column = self.get_children()[0]
            news_entries = NewsPage.objects.descendant_of(first_column).live().order_by('-date')
            context[first_column.slug + '_entries'] = news_entries
        return context

    # def get_context(self, request):
    #     context = super(NewsIndexPage, self).get_context(request)
    #     for column in self.get_children():
    #         if column.slug:
    #             column_page = self.get_children().get(slug=column.slug)
    #             news_entries = NewsPage.objects.descendant_of(column_page).live().order_by('-date')
    #             context[column.slug + '_entries'] = news_entries
    #     return context



class BusinessIndexPage(Page):
    class Meta:
        verbose_name = "集团业务二级页面"

    subpage_types = ['ColumnPage']
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(BusinessIndexPage, self).get_context(request)
        column_entries = self.get_children().specific()
        context['column_entries'] = column_entries
        business = []
        enterprise = []
        for col in column_entries:
            for item in col.get_children().specific():
                if isinstance(item, BusinessDomain):
                    business.append(item)
                elif isinstance(item, EnterprisePage):
                    enterprise.append(item)
        context['business'] = business
        context['enterprise'] = enterprise
        return context

class PartyBuildingIndexPage(Page):
    class Meta:
        verbose_name = "党建工作二级页面"
        
    subpage_types = ['ColumnPage', 'FormPage']
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class EnterpriseCultureIndexPage(Page):
    class Meta:
        verbose_name = "企业文化二级页面"

    subpage_types = ['ColumnPage']
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class AcademyIndexPage(Page):
    class Meta:
        verbose_name = "金控学院二级页面"

    subpage_types = ['ColumnPage']
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ContactUsIndexPage(Page):
    class Meta:
        verbose_name = "联系我们二级页面"

    subpage_types = ['ColumnPage']
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ColumnPage(Page):
    class Meta:
        verbose_name = "专栏"
        
    subpage_types = ['NewsPage', 'BusinessDomain', 'EnterprisePage', 'FundPage', 'WebsiteLinkPage', 'VideoPage', 'FormPage']
    intro = RichTextField(blank=True)


    def get_context(self, request):
        context = super(ColumnPage, self).get_context(request)
        if self.slug:
            news_entries = NewsPage.objects.descendant_of(self).live().order_by('-date')
            context['column_entries'] = news_entries
            pages = Paginator(news_entries, 10)
            page = request.GET.get('page', 1)
            # Should use try catch here
            page_entries = pages.page(int(page))
            context['page_entries'] = page_entries

        if request.path == '/business/domain' or request.path == '/business/investment' or request.path == '/business/fund':
            column_entries = self.get_children()
            context['column_entries'] = column_entries
        return context

    
    def serve(self, request):
        if request.path == '/business/domain':
            return render(request, 'news/business_domain.html', self.get_context(request))
        elif request.path == '/business/investment':
            return render(request, 'news/enterprise_page.html', self.get_context(request))
        elif request.path == '/business/fund':
            return render(request, 'news/fund_page.html', self.get_context(request))
        else:
            return render(request, 'news/column_page.html', self.get_context(request))
    

class NewsPage(Page):
    class Meta:
        verbose_name = "新闻"

    NEWS_CATEGORY = (
        ("thumbnail", "图片内容"),
        ("textonly", "文本内容"),
        ("video", "视频内容"),
        ("singlepage", "单页内容"),)

    
    news_category = models.CharField(max_length=10, choices=NEWS_CATEGORY, default=1, verbose_name="内容类型")
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
        FieldPanel('news_category'),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

class VideoPage(Page):
    class Meta:
        verbose_name = "视频内容"
    date = models.DateField(verbose_name="日期")
    video_file_name = models.CharField(max_length=250, verbose_name="视频文件名称")
    intro = models.CharField(max_length=250, verbose_name="简介")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('video_file_name'),
        FieldPanel('intro'),]

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
        context['column_entries'] = column_entries
        return context

class FundPage(Page):
    class Meta:
        verbose_name = "基金管理"

    ENTERPRISE_CATEGORY = (
        ("产业基金", "产业基金"),
        ("其他基金", "其他基金"),)

    
    fund_category = models.CharField(max_length=10, choices=ENTERPRISE_CATEGORY, default=1, verbose_name="基金类型")   
    fund_name = models.CharField(max_length=60, verbose_name="基金名称")
    fund_intro = RichTextField(blank=True, verbose_name="基金简介")
    fund_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logo"
    )
    fund_website = models.CharField(blank=True, max_length=200, verbose_name="网址")

    content_panels = Page.content_panels + [
        FieldPanel('fund_category'),
        FieldPanel('fund_name'),
        FieldPanel('fund_intro'),
        ImageChooserPanel('fund_logo'),
        FieldPanel('fund_website'),
    ]

    def get_context(self, request):
        context = super(FundPage, self).get_context(request)
        column_entries = self.get_children()
        context['column_entries'] = column_entries
        return context

class BusinessDomain(Page):
    class Meta:
        verbose_name = "业务领域"

    BUSINESS_CATEGORY = (
        ("1主金融", "1主金融"),
        ("2类金融", "2类金融"),
        ("3平台类", "3平台类"),
        ("4其他类", "4其他类"),)

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


class WebsiteLinkPage(Page):
    class Meta:
        verbose_name = "网站链接"
    LINK_CATEGORY = (
        ("友情链接", "友情链接"),
        ("集团链接", "集团链接"),)
    
    link_category = models.CharField(max_length=10, choices=LINK_CATEGORY, default=1, verbose_name="链接类型")   
    site_name = models.CharField(max_length=60, verbose_name="链接名称")
    link_href = models.CharField(max_length=200, verbose_name="网址")

    content_panels = Page.content_panels + [
        FieldPanel('link_category'),
        FieldPanel('site_name'),
        FieldPanel('link_href'),]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')

    content_panels = AbstractForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
    ]


class FormPage(AbstractForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full")
    ]

    def get_context(self, request):
        context = super(FormPage, self).get_context(request)
        context['form_entry'] = self
        return context

    def serve(self, request):
        if request.method == 'GET':
            return render(request, 'news/column_page.html', self.get_context(request))

        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
            if form.is_valid():
                self.process_form_submission(form)
                messages.success(request, '您的信函投递成功!')
            return render(request, 'news/column_page.html', self.get_context(request))