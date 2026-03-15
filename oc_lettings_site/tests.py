from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    """Tests pour la vue d'accueil."""

    def test_home_view(self):
        """Teste la vue d'accueil."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Holiday Homes')

    def test_home_view_template(self):
        """Teste que le bon template est utilisé."""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')


class ErrorPagesTest(TestCase):
    """Tests pour les pages d'erreur."""

    def test_404_page(self):
        """Teste la page d'erreur 404."""
        response = self.client.get('/page-inexistante/')
        self.assertEqual(response.status_code, 404)
