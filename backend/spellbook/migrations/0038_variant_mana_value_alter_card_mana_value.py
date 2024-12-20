# Generated by Django 5.1.1 on 2024-12-20 15:09

from django.db import migrations, models


def init_mana_values(apps, schema_editor):
    Variant = apps.get_model('spellbook', 'Variant')
    Variant.objects.update(mana_value=models.Subquery(
        Variant.objects.filter(pk=models.OuterRef('pk')).annotate(
            computed_mana_value=models.Sum('uses__mana_value')
        ).values('computed_mana_value')[:1]
    ))


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0037_support_premodern_and_duplicate_features_in_combo'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='mana_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='mana_value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.RunPython(
            code=init_mana_values,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
