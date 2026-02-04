from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error),  # Route de test Sentry
]

# Handlers pour les erreurs
handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'
