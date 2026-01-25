from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    """Tests pour le modèle Address."""

    def setUp(self):
        """Créer une adresse de test."""
        self.address = Address.objects.create(
            number=123,
            street='Main Street',
            city='New York',
            state='NY',
            zip_code=10001,
            country_iso_code='USA'
        )

    def test_address_str(self):
        """Teste la représentation string d'une adresse."""
        self.assertEqual(str(self.address), '123 Main Street')

    def test_address_creation(self):
        """Teste la création d'une adresse."""
        self.assertEqual(self.address.city, 'New York')
        self.assertEqual(self.address.state, 'NY')


class LettingModelTest(TestCase):
    """Tests pour le modèle Letting."""

    def setUp(self):
        """Créer une location de test."""
        self.address = Address.objects.create(
            number=456,
            street='Oak Avenue',
            city='Los Angeles',
            state='CA',
            zip_code=90001,
            country_iso_code='USA'
        )
        self.letting = Letting.objects.create(
            title='Beautiful Apartment',
            address=self.address
        )

    def test_letting_str(self):
        """Teste la représentation string d'une location."""
        self.assertEqual(str(self.letting), 'Beautiful Apartment')

    def test_letting_address_relationship(self):
        """Teste la relation avec Address."""
        self.assertEqual(self.letting.address, self.address)


class LettingsViewsTest(TestCase):
    """Tests pour les vues de l'application lettings."""

    def setUp(self):
        """Créer des données de test."""
        self.address = Address.objects.create(
            number=789,
            street='Park Lane',
            city='Chicago',
            state='IL',
            zip_code=60601,
            country_iso_code='USA'
        )
        self.letting = Letting.objects.create(
            title='Cozy Studio',
            address=self.address
        )

    def test_lettings_index_view(self):
        """Teste la vue index des lettings."""
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lettings')
        self.assertContains(response, 'Cozy Studio')

    def test_letting_detail_view(self):
        """Teste la vue détail d'une location."""
        response = self.client.get(
            reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cozy Studio')
        self.assertContains(response, '789 Park Lane')


class LettingsUrlsTest(TestCase):
    """Tests pour les URLs de l'application lettings."""

    def test_lettings_index_url(self):
        """Teste l'URL de l'index des lettings."""
        url = reverse('lettings:index')
        self.assertEqual(url, '/lettings/')

    def test_letting_detail_url(self):
        """Teste l'URL de détail d'une location."""
        url = reverse('lettings:letting', kwargs={'letting_id': 1})
        self.assertEqual(url, '/lettings/1/')
