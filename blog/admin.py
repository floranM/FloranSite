from django.contrib import admin

# Register your models here.
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from .models import BlogPage, BlogTag, SocialLink, Author
from home.models import FooterUn, FooterDeux
from taggit.models import TaggedItemBase, Tag

class BlogPageAdmin(ModelAdmin):
    model = BlogPage  # Spécifiez le modèle à administrer
    menu_label = "Articles de Blog"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "doc-empty"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('title', 'IsFeatured', 'locale', 'live', 'date', 'first_published_at')  # Les colonnes dans la liste
    list_filter = ('locale', 'live', 'IsFeatured', 'tags')  # Les colonnes dans la liste
    search_fields = ('title', 'intro')  # Champs disponibles pour la recherche

class TagAdmin(ModelAdmin):
    model = BlogTag  # Spécifiez le modèle à administrer
    menu_label = "Tags"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "tag"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')  # Champs disponibles pour la

class AuthorAdmin(ModelAdmin):
    model = Author  # Spécifiez le modèle à administrer
    menu_label = "Auteurs"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "user"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('name', 'view_name', 'url')
    search_fields = ('name')  # Champs disponibles pour la recherche
    list_filter = ('name', 'url')  # Les colonnes dans la liste

# Groupe ModelAdmin
class GestionBlogGroup(ModelAdminGroup):
    menu_label = "Blog"  # Nom du groupe dans le menu
    menu_icon = "form"  # Icône du groupe
    items = [BlogPageAdmin, TagAdmin, AuthorAdmin]  # Admins inclus dans le groupe

# Enregistrement du groupe
modeladmin_register(GestionBlogGroup)

class SocialLinkAdmin(ModelAdmin):
    model = SocialLink
    menu_icon = "link"
    menu_label = "Liens sociaux"
    list_display = ("titre", "position", "url", "follow", "icon")
    list_filter = ("follow", "url", 'titre')
    search_fields = ("titre")  # Ajout d'un champ de recherche

class FooterUnAdmin(ModelAdmin):
    model = FooterUn
    menu_icon = "doc-empty"
    menu_label = "Footer Un"
    list_display = ("title",)
    search_fields = ("title",)  # Ajout d'un champ de recherche


class FooterDeuxAdmin(ModelAdmin):
    model = FooterDeux
    menu_icon = "doc-empty"
    menu_label = "Footer Deux"
    list_display = ("title",)
    search_fields = ("title",)  # Ajout d'un champ de recherche

# Groupe ModelAdmin
class ParametreGroup(ModelAdminGroup):
    menu_label = "Parametres Site"  # Nom du groupe dans le menu
    menu_icon = "cogs"  # Icône du groupe
    items = [SocialLinkAdmin, FooterUnAdmin, FooterDeuxAdmin]  # Admins inclus dans le groupe

# Enregistrement du groupe
modeladmin_register(ParametreGroup)