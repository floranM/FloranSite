from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageBlock
from blog.models import BlogPage, BlogIndexPage

class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        current_locale = self.locale
        featured_posts = BlogPage.objects.live().filter(IsFeatured=True, locale=current_locale).order_by('?')
        if featured_posts:
            context["featured_posts"] = featured_posts
        else:
            context["featured_posts"] = 'fuck'
        blog_index_page = BlogIndexPage.objects.filter(locale=current_locale).first()
        context['blog_index_url'] = blog_index_page.url if blog_index_page else None
        return context
     
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', blocks.TextBlock()),
    ], blank=True)
    body = RichTextField(blank=True)
    

    content_panels = Page.content_panels + [FieldPanel('intro'), "body"]

   
    

class AboutPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body"]