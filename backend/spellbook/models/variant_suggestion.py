from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField
from .mixins import ScryfallLinkMixin
from .card import Card
from .template import Template
from .feature import Feature
from .variant import Variant
from .ingredient import IngredientInCombination
from .validators import TEXT_VALIDATORS, MANA_VALIDATOR, FIRST_CAPITAL_LETTER_VALIDATOR, ORDINARY_CHARACTERS_VALIDATOR
from .utils import recipe, id_from_cards_and_templates_ids


class VariantSuggestion(models.Model):
    class Status(models.TextChoices):
        NEW = 'N'
        ACCEPTED = 'A'
        REJECTED = 'R'

    status = models.CharField(choices=Status.choices, default=Status.NEW, help_text='Suggestion status for editors', max_length=2)
    mana_needed = models.CharField(blank=True, max_length=200, default='', help_text='Mana needed for this combo. Use the {1}{W}{U}{B}{R}{G}{B/P}... format.', validators=[MANA_VALIDATOR])
    other_prerequisites = models.TextField(blank=True, default='', help_text='Other prerequisites for this variant.', validators=TEXT_VALIDATORS)
    description = models.TextField(blank=True, help_text='Long description, in steps', validators=TEXT_VALIDATORS)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    suggested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, help_text='User that suggested this variant', related_name='variants')

    class Meta:
        ordering = ['-status', '-created']
        verbose_name = 'variant suggestion'
        verbose_name_plural = 'variant suggestions'

    def __str__(self):
        if self.pk is None:
            return f'New variant suggestion with unique id <{self.id}>'
        produces = list(self.produces.all()[:4])
        return recipe([str(use.card) for use in self.uses.all()] + [str(require.template) for require in self.requires.all()], [str(produce.feature) for produce in produces])

    @classmethod
    def validate(cls, cards: list[str], templates: list[str]):
        card_entities = list(Card.objects.filter(name__in=cards))
        template_entities = list(Template.objects.filter(name__in=templates))
        if len(card_entities) == len(cards) \
            and len(template_entities) == len(templates):
            variant_id = id_from_cards_and_templates_ids([card.id for card in card_entities], [template.id for template in template_entities])
            if Variant.objects.filter(id=variant_id).exists():
                raise ValidationError('This variant already exists.')
        if VariantSuggestion.objects.filter(uses__card__in=cards, requires__template__in=templates).exists():
            raise ValidationError(f'This variant suggestion is redundant given suggestion.')


class CardUsedInVariantSuggestion(IngredientInCombination):
    card = models.CharField(max_length=128, blank=False, help_text='Card name', verbose_name='card name', validators=[ORDINARY_CHARACTERS_VALIDATOR])
    variant = models.ForeignKey(to=VariantSuggestion, on_delete=models.CASCADE, related_name='uses')

    def __str__(self):
        return self.card

    class Meta(IngredientInCombination.Meta):
        unique_together = [('card', 'variant')]


class TemplateRequiredInVariantSuggestion(IngredientInCombination):
    template = models.CharField(max_length=128, blank=False, help_text='Template name', verbose_name='template name', validators=[ORDINARY_CHARACTERS_VALIDATOR])
    variant = models.ForeignKey(to=VariantSuggestion, on_delete=models.CASCADE, related_name='requires')

    def __str__(self):
        return self.template

    class Meta(IngredientInCombination.Meta):
        unique_together = [('template', 'variant')]


class FeatureProducedInVariantSuggestion(models.Model):
    feature = models.CharField(max_length=128, blank=False, help_text='Feature name', verbose_name='feature name', validators=[ORDINARY_CHARACTERS_VALIDATOR, FIRST_CAPITAL_LETTER_VALIDATOR])
    variant = models.ForeignKey(to=VariantSuggestion, on_delete=models.CASCADE, related_name='produces')

    def __str__(self):
        return self.feature

    class Meta:
        unique_together = [('feature', 'variant')]
        ordering = ['feature', 'id']