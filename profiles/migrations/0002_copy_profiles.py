from django.db import migrations


def copy_profiles(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    # Sécurité : on évite les doublons si la migration est rejouée (rare mais pratique)
    existing_user_ids = set(NewProfile.objects.values_list("user_id", flat=True))
    to_create = []

    # On ne copie que les colonnes nécessaires.
    for p in OldProfile.objects.all().only("user_id", "favorite_city"):
        if p.user_id in existing_user_ids:
            continue
        to_create.append(NewProfile(user_id=p.user_id, favorite_city=p.favorite_city))

    # OneToOne -> un enregistrement par user. bulk_create est parfait ici.
    if to_create:
        NewProfile.objects.bulk_create(to_create, ignore_conflicts=True)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
        # cette dépendance garantit que l'ancien modèle existe quand on copie
        ("oc_lettings_site", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(copy_profiles, noop_reverse),
    ]
