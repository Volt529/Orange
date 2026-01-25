from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil du site.

    Args:
        request: La requête HTTP

    Returns:
        HttpResponse: La page d'accueil
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Affiche une page d'erreur 404 personnalisée.

    Args:
        request: La requête HTTP
        exception: L'exception levée

    Returns:
        HttpResponse: La page d'erreur 404
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Affiche une page d'erreur 500 personnalisée.

    Args:
        request: La requête HTTP

    Returns:
        HttpResponse: La page d'erreur 500
    """
    return render(request, '500.html', status=500)


def trigger_error(request):
    """
    Vue de test pour déclencher une erreur et tester Sentry.

    Args:
        request: La requête HTTP

    Raises:
        Exception: Une erreur de test
    """
    division_by_zero = 1 / 0
    return division_by_zero