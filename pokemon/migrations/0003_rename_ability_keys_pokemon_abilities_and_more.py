# Generated by Django 5.1.5 on 2025-01-22 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon_uri'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='ability_keys',
            new_name='abilities',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='move_keys',
            new_name='moves',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='type_keys',
            new_name='types',
        ),
        migrations.RenameField(
            model_name='pokemonmove',
            old_name='type_key',
            new_name='type',
        ),
    ]
