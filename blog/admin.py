from django.contrib import admin

# Register your models here.
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

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


# Groupe ModelAdmin
class GestionBlogGroup(ModelAdminGroup):
    menu_label = "Blog"  # Nom du groupe dans le menu
    menu_icon = "form"  # Icône du groupe
    items = [BlogPageAdmin, TagAdmin]  # Admins inclus dans le groupe

# Enregistrement du groupe
modeladmin_register(GestionBlogGroup)

class SocialLinkAdmin(ModelAdmin):
    model = SocialLink
    menu_icon = "link"
    menu_label = "Liens sociaux"
    list_display = ("titre", "position", "url", "follow", "icon")
    list_filter = ("follow", "url", 'titre')
    search_fields = ("titre")  # Ajout d'un champ de recherche





# Groupe ModelAdmin
class ParametreGroup(ModelAdminGroup):
    menu_label = "Parametres Site"  # Nom du groupe dans le menu
    menu_icon = "cogs"  # Icône du groupe
    items = [SocialLinkAdmin]  # Admins inclus dans le groupe

# Enregistrement du groupe
modeladmin_register(ParametreGroup)