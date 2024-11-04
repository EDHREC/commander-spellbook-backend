# Generated by Django 5.1.1 on 2024-11-04 10:02

from django.db import migrations, models


def transfer_status(apps, schema_editor):
    VariantSuggestion = apps.get_model('spellbook', 'VariantSuggestion')
    VariantSuggestion.objects.filter(status='NR').update(status='AD')
    VariantSuggestion.objects.filter(status='RE').update(status='PA')


def reverse_transfer_status(apps, schema_editor):
    VariantSuggestion = apps.get_model('spellbook', 'VariantSuggestion')
    VariantSuggestion.objects.filter(status='AD').update(status='NR')
    VariantSuggestion.objects.filter(status='PA').update(status='RE')


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0035_variant_variant_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantsuggestion',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('AD', 'Awaiting Discussion'), ('PA', 'Pending Approval'), ('A', 'Accepted'), ('R', 'Rejected')], default='N', help_text='Suggestion status for editors', max_length=2),
        ),
        migrations.RunPython(code=transfer_status, reverse_code=reverse_transfer_status),
        migrations.AlterModelOptions(
            name='featureattribute',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='variantsuggestion',
            options={'default_manager_name': 'objects', 'ordering': [models.Case(models.When(status='N', then=models.Value(0)), models.When(status='PA', then=models.Value(1)), models.When(status='AD', then=models.Value(2)), models.When(status='A', then=models.Value(3)), models.When(status='R', then=models.Value(4)), default=models.Value(10)), 'created'], 'verbose_name': 'variant suggestion', 'verbose_name_plural': 'variant suggestions'},
        ),
    ]
