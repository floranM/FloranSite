from django import template
from django.utils.translation import get_language
from wagtail.models import Page, Site, Locale  # Importer Locale pour gérer les traductions

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # Vérifier si la requête existe dans le contexte
    request = context.get("request")
    if not request:
        return None

    # Trouver le site correspondant à la requête
    site = Site.find_for_request(request)
    if not site:
        return None

    # Récupérer la page racine
    site_root = site.root_page
    if not site_root:
        return None

    # Obtenir la langue actuelle
    current_language = get_language()

    # Rechercher l'objet Locale correspondant à la langue actuelle
    try:
        current_locale = Locale.objects.get(language_code=current_language)
    except Locale.DoesNotExist:
        return site_root  # Retourner la page racine par défaut si la langue n'existe pas

    # Rechercher la traduction de la page racine dans la langue actuelle
    translated_root = site_root.get_translation_or_none(locale=current_locale)

    # Retourner la page traduite ou la page racine par défaut si aucune traduction n'est trouvée
    return translated_root or site_root