from django.db import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
    )
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from django.contrib import messages

from django import forms
from captcha.fields import CaptchaField
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json

# from django.core.mail import send_mail
from smtplib import SMTPException
from mail_templated import send_mail

from .ueditor_richtext_field import UEditorRichTextField

# from wagtail.wagtailcore.fields import StreamField
# from wagtail.wagtailcore import blocks
# from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel


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
        
    subpage_types = ['ColumnPage', 'FormPage', 'PartybuildingTheories' ]
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

class ContactUs(Page):
    class Meta:
        verbose_name = "联系我们地图"
    

class IndustrialDevelopmentFundIndexPage(Page):
    class Meta:
        verbose_name = "产业发展基金二级页面"
    subpage_types = ['IndustrialDevelopmentFundColumnPage']
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ColumnPage(Page):
    class Meta:
        verbose_name = "专栏"
        
    subpage_types = ['NewsPage', 'BusinessDomain', 'EnterprisePage', 'FundPage', 'IndustrialDevelopmentFund' ,'WebsiteLinkPage', 'VideoPage', 'FormPage', 'ContactUs' , 'PartybuildingTheories']
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

class IndustrialDevelopmentFundColumnPage(Page):
    class Meta:
        verbose_name = "产业发展投资基金专栏"
        
    subpage_types = ['IndustrialDevelopmentFund']
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super(IndustrialDevelopmentFundColumnPage, self).get_context(request)
        fund_column_entries = self.get_children()
        context['fund_column_entries'] = fund_column_entries
        context['form'] = IndustrialDevelopmentFundForm()
        return context
    
    def serve(self, request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = IndustrialDevelopmentFundForm(request.POST)
            
            idfund = {}
            # check whether it's valid:
            if form.is_valid():
                idfund['idfund_invest_doamin'] = form.cleaned_data['idfund_invest_doamin']
                idfund['idfund_company_name'] = form.cleaned_data['idfund_company_name']
                idfund['idfund_contact_name'] = form.cleaned_data['idfund_contact_name']
                idfund['idfund_contact_phone'] = form.cleaned_data['idfund_contact_phone']
                idfund['idfund_contact_email'] = form.cleaned_data['idfund_contact_email']
                idfund['idfund_project_demand'] = form.cleaned_data['idfund_project_demand']
                send_mail('news/mail_template.html', {'idfund': idfund}, 'web@gsjkjt.com', ['jjglb@gsjkjt.com'])
                result = True 
            else:
                result = False

        # if a GET (or any other method) we'll create a blank form
        else:
            form = IndustrialDevelopmentFundForm()
            return render(request, 'news/industrial_development_fund_column_page.html', self.get_context(request))
        return  HttpResponse(json.dumps({'result': result}), content_type='application/json')  
        # return render(request, 'news/industrial_development_fund_column_page.html', self.get_context(request))

class NewsPage(Page):
    class Meta:
        verbose_name = "新闻"

    NEWS_CATEGORY = (
        ("thumbnail", "图片内容"),
        ("textonly", "文本内容"),
        ("video", "视频内容"),
        ("singlepage", "单页内容"),)

    
    news_category = models.CharField(max_length=30, choices=NEWS_CATEGORY, default=1, verbose_name="内容类型")
    date = models.DateField(verbose_name="日期")
    intro = models.CharField(max_length=250, verbose_name="简介")
    body = RichTextField(blank=True, verbose_name="内容")
    extro = UEditorRichTextField(blank=True)
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
        FieldPanel('extro'),
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

class IndustrialDevelopmentFund(Page):
    class Meta:
        verbose_name = "产业发展投资基金"
    fund_name = models.CharField(max_length=60, verbose_name="产业发展投资基金名称")
    fund_intro = RichTextField(blank=True, verbose_name="产业发展投资基金简介")
    fund_intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="产业发展基金图片")

    content_panels = Page.content_panels + [
        FieldPanel('fund_name'),
        FieldPanel('fund_intro'),
        ImageChooserPanel('fund_intro_image'),]


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

class PartybuildingTheories(Page):
    class Meta:
        verbose_name = "理论苑地"
    theory_name = models.CharField(max_length=60, verbose_name="名称")
    theory_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="背景图片")
    link_href = models.CharField(max_length=200, verbose_name="链接地址")

    content_panels = Page.content_panels + [
        FieldPanel('theory_name'),
        ImageChooserPanel('theory_image'),
        FieldPanel('link_href'),]

    def get_context(self, request):
        context = super(PartybuildingTheories, self).get_context(request)
        column_entries = self.get_children()
        context['column_entries'] = column_entries
        return context


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



class IndustrialDevelopmentFundForm(forms.Form):
    idfund_invest_doamin = forms.CharField(widget=forms.TextInput(attrs={'class' : 'idfund-form-input'}), label='投资方向', max_length=80)
    idfund_company_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'idfund-form-input'}), label='公司名称', max_length=50)
    idfund_contact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'idfund-form-input'}), label='联系人', max_length=20)
    idfund_contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'idfund-form-input'}), label='联系人电话', max_length=20)
    idfund_contact_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'idfund-form-input'}), label='联系人邮箱', max_length=30)
    idfund_project_demand = forms.CharField(widget=forms.Textarea(attrs={'class': 'pull-left', 'cols': "60", 'rows': "12", 'validator': 'required'}), label='项目需求', max_length=600)
    captcha = CaptchaField(label='验证码')
