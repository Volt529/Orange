from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configuration de l'interface admin pour Profile."""
    list_display = ('user', 'favorite_city')
