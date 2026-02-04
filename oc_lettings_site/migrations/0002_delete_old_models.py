from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),  # Adapte selon ton dernier numéro
        ('lettings', '0002_copy_data'),
        ('profiles', '0002_copy_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]