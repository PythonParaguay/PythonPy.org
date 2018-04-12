from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class DefaultPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('table', TableBlock()),

    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]
