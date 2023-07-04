# Generated by Django 4.2.1 on 2023-07-04 09:42

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0009_card_name_unaccented'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='feature',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='name_unique_ci', violation_error_message='Feature name should be unique, ignoring case.'),
        ),
    ]
