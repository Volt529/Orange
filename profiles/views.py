from django.shortcuts import render
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la liste de tous les profils utilisateurs.

    Args:
        request: La requête HTTP

    Returns:
        HttpResponse: La page avec la liste des profils
    """
    logger.info("Accès à la page index des profiles")
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des profiles: {e}")
        raise


def profile(request, username):
    """
    Affiche le profil d'un utilisateur spécifique.

    Args:
        request: La requête HTTP
        username: Le nom d'utilisateur

    Returns:
        HttpResponse: La page du profil utilisateur
    """
    logger.info(f"Accès au profil de l'utilisateur {username}")
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f"Profil {username} introuvable")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du profil {username}: {e}")
        raise
