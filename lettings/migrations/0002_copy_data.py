from django.db import migrations


def copy_lettings_data(apps, schema_editor):
    """Copie les données de oc_lettings_site vers lettings."""
    # Les données ont déjà été migrées, cette migration est optionnelle
    # pour les nouvelles installations
    try:
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
        OldLetting = apps.get_model('oc_lettings_site', 'Letting')
        
        NewAddress = apps.get_model('lettings', 'Address')
        NewLetting = apps.get_model('lettings', 'Letting')
        
        # Copier les adresses
        for old_address in OldAddress.objects.all():
            NewAddress.objects.create(
                id=old_address.id,
                number=old_address.number,
                street=old_address.street,
                city=old_address.city,
                state=old_address.state,
                zip_code=old_address.zip_code,
                country_iso_code=old_address.country_iso_code
            )
        
        # Copier les lettings
        for old_letting in OldLetting.objects.all():
            NewLetting.objects.create(
                id=old_letting.id,
                title=old_letting.title,
                address_id=old_letting.address_id
            )
    except LookupError:
        # Les anciens modèles n'existent plus, on skip
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_lettings_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]