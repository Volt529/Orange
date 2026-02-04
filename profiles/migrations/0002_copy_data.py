from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    """Copie les données de oc_lettings_site vers profiles."""
    try:
        OldProfile = apps.get_model('oc_lettings_site', 'Profile')
        NewProfile = apps.get_model('profiles', 'Profile')
        
        for old_profile in OldProfile.objects.all():
            NewProfile.objects.create(
                id=old_profile.id,
                user_id=old_profile.user_id,
                favorite_city=old_profile.favorite_city
            )
    except LookupError:
        # Les anciens modèles n'existent plus, on skip
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_profiles_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]