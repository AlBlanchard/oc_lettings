from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("oc_lettings_site", "0002_auto_20250903_1154"),
        (
            "profiles",
            "0002_copy_profiles",
        ),  # assure que la copie est faite avant suppression
    ]
    operations = [
        migrations.DeleteModel(name="Profile"),
    ]
