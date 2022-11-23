# Generated by Django 2.2.28 on 2022-11-23 19:22

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180412_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock())], icon='arrow-left', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock())], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('custom_table', wagtail.core.blocks.StructBlock([('custom_table', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('table_intro', wagtail.core.blocks.RichTextBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'colHeaders': True, 'height': 108, 'language': 'en', 'rowHeaders': True, 'startCols': 6, 'startRows': 7})), ('footnote', wagtail.core.blocks.CharBlock(required=False))]))])), ('thumbnail', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='excerpt',
            field=models.CharField(blank=True, max_length=250, verbose_name='Extracto'),
        ),
    ]
