from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.table_block.blocks import TableBlock


class CustomTableBlock(blocks.StructBlock):
    """A custom table"""
    custom_table_options = {
        'startRows': 7,
        'startCols': 6,
        'colHeaders': True,
        'rowHeaders': True,
        'height': 108,
        'language': 'en',
    }

    custom_table = blocks.StreamBlock([
        ('title', blocks.CharBlock(required=False)),
        ('table_intro', blocks.RichTextBlock(required=False)),
        ('table', TableBlock(table_options=custom_table_options)),
        ('footnote', blocks.CharBlock(required=False))
    ])

    class Meta:
        template = 'blocks/custom_table.html'


class TwoColumnBlock(blocks.StructBlock):
    COLOUR_CHOICES = ('wjthe',
                      'black',
                      'gray')
    # background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.TextBlock(required=False)

    class Meta:
        icon = 'image'
