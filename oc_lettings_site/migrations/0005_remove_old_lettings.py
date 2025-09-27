from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("oc_lettings_site", "0004_profile"),
        ("lettings", "0002_copy_addresses_and_lettings"),
    ]
    operations = [
        migrations.DeleteModel(name="Letting"),
        migrations.DeleteModel(name="Address"),
    ]
