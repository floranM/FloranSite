from django.contrib import admin

# Register your models here.
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import BlogPage, BlogTag
from taggit.models import TaggedItemBase, Tag

class BlogPageAdmin(ModelAdmin):
    model = BlogPage  # Spécifiez le modèle à administrer
    menu_label = "Articles de Blog"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "doc-empty"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('title', 'IsFeatured', 'locale', 'live', 'date', 'first_published_at')  # Les colonnes dans la liste
    list_filter = ('locale', 'live', 'IsFeatured', 'tags')  # Les colonnes dans la liste
    search_fields = ('title', 'intro')  # Champs disponibles pour la recherche

# Enregistrez cette classe dans l'administration
modeladmin_register(BlogPageAdmin)

class TagAdmin(ModelAdmin):
    model = BlogTag  # Spécifiez le modèle à administrer
    menu_label = "Tags"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "tag"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')  # Champs disponibles pour la

modeladmin_register(TagAdmin)

