from django.db import migrations


def copy_addresses_and_lettings(apps, schema_editor):
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    # Copie les Address une par une et construire une map old_id -> new_id
    id_map = {}
    for a in OldAddress.objects.all().iterator():
        new = NewAddress.objects.create(
            number=a.number,
            street=a.street,
            city=a.city,
            state=a.state,
            zip_code=a.zip_code,
            # getattr pour compat « ancien schéma sans country »
            country_iso_code=getattr(a, "country_iso_code", None),
        )
        id_map[a.pk] = new.pk

    # Copie les Letting en reconnectant la FK via la map
    to_create = []
    for l in OldLetting.objects.all().iterator():
        to_create.append(
            NewLetting(
                title=l.title,
                address_id=id_map.get(l.address_id),
            )
        )
    if to_create:
        NewLetting.objects.bulk_create(to_create)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0004_profile"),
    ]
    operations = [
        migrations.RunPython(copy_addresses_and_lettings, noop),
    ]
