from datetime import  datetime
from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel, MultiFieldPanel,
                                         StreamFieldPanel, PageChooserPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.search import index

from .blocks import (TwoColumnBlock, CustomTableBlock,
                     ThumbnailBlock)

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # update context to include only published posts and in reverse order
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogTagIndexPage(Page):

    def get_context(self, request):
        # filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        # update context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


# TODO create profile for authors

class BlogPage(Page):
    date = models.DateField("Post date", default=datetime.today)
    excerpt = models.CharField('Extracto', max_length=250, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('table', TableBlock()),
        ('custom_table', CustomTableBlock()),
        ('thumbnail', ThumbnailBlock()),

    ], null=True, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        return None

    search_fields = Page.search_fields + [
        index.SearchField('excerpt'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog info"),

        FieldPanel('excerpt'),
        StreamFieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)

    panel = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
