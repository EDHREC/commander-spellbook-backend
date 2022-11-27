# Generated by Django 4.1.2 on 2022-11-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0007_alter_template_scryfall_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='variants',
        ),
        migrations.AddField(
            model_name='variant',
            name='generated_by',
            field=models.ForeignKey(blank=True, editable=False, help_text='Job that generated this variant', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variants', to='spellbook.job'),
        ),
    ]
