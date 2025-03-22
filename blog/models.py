from django.db import models

# Add these:
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import MultiFieldPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TagBase, ItemBase

from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageBlock

from wagtail.search import index





class BlogIndexPage(Page):
    subpage_types = ['BlogPage']  # Limite les enfants à BlogPage uniquement
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + ["intro"]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        current_locale = self.locale
        context = super().get_context(request)
        blogpages = self.get_children().live().filter(locale=current_locale).order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


@register_snippet
class BlogTag(TagBase):
    class Meta:
        verbose_name = "blog tag"
        verbose_name_plural = "blog tags"


class TaggedBlog(ItemBase):
    tag = models.ForeignKey(
        BlogTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to='BlogPage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )

class BlogPage(Page):
    parent_page_types = ['BlogIndexPage']
    
    date = models.DateTimeField("Post date")
    intro = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', blocks.TextBlock()),
        ('image', ImageBlock()),
    ], blank=True)
    
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    authors = ParentalManyToManyField('blog.Author', blank=True)
    
    tags = ClusterTaggableManager(through=TaggedBlog, blank=True)

    IsFeatured = models.BooleanField(default=False, verbose_name="Article en vedette")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('IsFeatured'),
    ]

    content_panels = Page.content_panels + [MultiFieldPanel(["date", "authors"]), "intro", "body", FieldPanel('image'), FieldPanel('tags')]
    promote_panels = Page.promote_panels + [FieldPanel('IsFeatured'),]



@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    view_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    bio = RichTextField(blank=True)

    panels = ["name","view_name", "bio", "author_image", "url"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'