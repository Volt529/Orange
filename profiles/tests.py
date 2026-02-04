from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    """Tests pour le modèle Profile."""

    def setUp(self):
        """Créer un profil de test."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='John',
            last_name='Doe',
            email='john@example.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_profile_str(self):
        """Teste la représentation string d'un profil."""
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_creation(self):
        """Teste la création d'un profil."""
        self.assertEqual(self.profile.favorite_city, 'Paris')
        self.assertEqual(self.profile.user.username, 'testuser')

    def test_profile_user_relationship(self):
        """Teste la relation avec User."""
        self.assertEqual(self.profile.user, self.user)


class ProfilesViewsTest(TestCase):
    """Tests pour les vues de l'application profiles."""

    def setUp(self):
        """Créer des données de test."""
        self.user = User.objects.create_user(
            username='johndoe',
            password='secret',
            first_name='John',
            last_name='Doe',
            email='john@test.com'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='New York'
        )

    def test_profiles_index_view(self):
        """Teste la vue index des profiles."""
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profiles')
        self.assertContains(response, 'johndoe')

    def test_profile_detail_view(self):
        """Teste la vue détail d'un profil."""
        response = self.client.get(
            reverse('profiles:profile', kwargs={'username': 'johndoe'})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'johndoe')
        self.assertContains(response, 'New York')


class ProfilesUrlsTest(TestCase):
    """Tests pour les URLs de l'application profiles."""

    def test_profiles_index_url(self):
        """Teste l'URL de l'index des profiles."""
        url = reverse('profiles:index')
        self.assertEqual(url, '/profiles/')

    def test_profile_detail_url(self):
        """Teste l'URL de détail d'un profil."""
        url = reverse('profiles:profile', kwargs={'username': 'testuser'})
        self.assertEqual(url, '/profiles/testuser/')
