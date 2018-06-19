from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class AlignImageBlock(blocks.StructBlock):
    image =  ImageChooserBlock(required=True, classname="news-image", label="图片")
    image_caption = blocks.CharBlock(required=False, label="图片摘要")

    class Meta:
        template = 'wagtailadmin/align_image_block.html'
    