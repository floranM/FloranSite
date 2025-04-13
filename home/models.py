from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
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
        context['footerUn'] = FooterUn.objects.first()
        context['footerDeux'] = FooterDeux.objects.first()
        return context
     
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', blocks.TextBlock()),
    ], blank=True)
    body = RichTextField(blank=True)
    

    content_panels = Page.content_panels + [FieldPanel('intro'), "body"]

   
    

class StandardPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        current_locale = self.locale
        context['footerUn'] = FooterUn.objects.first()
        context['footerDeux'] = FooterDeux.objects.first()
        return context

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', blocks.TextBlock()),
        ('image', ImageChooserBlock())
        ])

    content_panels = Page.content_panels + ["body"]

class FooterUn(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = RichTextField(blank=True)
    def __str__(self):
        return self.title
    # Méthode pour contrôler la création
    def save(self, *args, **kwargs):
        if not self.pk and FooterUn.objects.exists():
            raise ValueError("Un seul enregistrement est autorisé.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Menu Footer 1, a enregistrement unique"

class FooterDeux(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = RichTextField(blank=True)
    # Méthode pour contrôler la création
    def save(self, *args, **kwargs):
        if not self.pk and FooterDeux.objects.exists():
            raise ValueError("Un seul enregistrement est autorisé.")
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Modèle à enregistrement unique"