from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de toutes les locations disponibles.

    Args:
        request: La requête HTTP

    Returns:
        HttpResponse: La page avec la liste des locations
    """
    logger.info("Accès à la page index des lettings")
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des lettings: {e}")
        raise


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Args:
        request: La requête HTTP
        letting_id: L'ID de la location

    Returns:
        HttpResponse: La page avec les détails de la location
    """
    logger.info(f"Accès aux détails de la location {letting_id}")
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"Location {letting_id} introuvable")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de la location {letting_id}: {e}")
        raise
