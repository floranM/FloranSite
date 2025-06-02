from django.contrib import admin

from wagtail_modeladmin.options import modeladmin_register, ModelAdminGroup
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from blog.models import Author
from home.models import FooterUn, FooterDeux



class MyTranslatableModelAdmin(TranslatableModelAdmin):
    model = Author
    menu_label = "Auteurs trad"  # Le nom qui apparaîtra dans le menu admin
    menu_icon = "user"  # Icône pour le menu (choisissez une icône de Wagtail)
    list_display = ('name', 'view_name', 'url')
    search_fields = ('name')  # Champs disponibles pour la recherche
    list_filter = ('name', 'url')  # Les colonnes dans la liste



class MyTranslatableModelFooterUnAdmin(TranslatableModelAdmin):
    model = FooterUn

class MytranslatableModelFooterDeuxAdmin(TranslatableModelAdmin):
    model = FooterDeux


class MyTranslatableGroup(ModelAdminGroup):
    menu_label = "Groupe de traduction"  # Nom du groupe dans le menu
    menu_icon = "cogs"  # Icône du groupe
    items = [MyTranslatableModelAdmin, MyTranslatableModelFooterUnAdmin, MytranslatableModelFooterDeuxAdmin]  # Admins inclus dans le groupe

modeladmin_register(MyTranslatableGroup)
