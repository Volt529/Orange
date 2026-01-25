from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Configuration de l'interface admin pour Address."""
    list_display = ('number', 'street', 'city', 'state', 'zip_code', 'country_iso_code')


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """Configuration de l'interface admin pour Letting."""
    list_display = ('title', 'address')
