from django.db import models
from sortedm2m.fields import SortedManyToManyField
from .playable import Playable
from .mixins import ScryfallLinkMixin, PreSaveModelMixin
from .card import Card
from .template import Template
from .feature import Feature
from .ingredient import IngredientInCombination
from .combo import Combo
from .job import Job
from .validators import TEXT_VALIDATORS, MANA_VALIDATOR
from .utils import recipe, mana_value


class Variant(Playable, PreSaveModelMixin, ScryfallLinkMixin):
    class Status(models.TextChoices):
        NEW = 'N'
        DRAFT = 'D'
        OK = 'OK'
        EXAMPLE = 'E'
        RESTORE = 'R'
        NOT_WORKING = 'NW'

    @classmethod
    def public_statuses(cls):
        return (cls.Status.OK, cls.Status.EXAMPLE)

    id = models.CharField(max_length=128, primary_key=True, unique=True, blank=False, help_text='Unique ID for this variant', editable=False)
    uses = models.ManyToManyField(
        to=Card,
        related_name='used_in_variants',
        help_text='Cards that this variant uses',
        editable=False,
        through='CardInVariant')
    requires = models.ManyToManyField(
        to=Template,
        related_name='required_by_variants',
        help_text='Templates that this variant requires',
        blank=True,
        verbose_name='required templates',
        through='TemplateInVariant')
    produces = SortedManyToManyField(
        to=Feature,
        related_name='produced_by_variants',
        help_text='Features that this variant produces',
        editable=False)
    includes = models.ManyToManyField(
        to=Combo,
        related_name='included_in_variants',
        help_text='Combo that this variant includes',
        editable=False)
    of = models.ManyToManyField(
        to=Combo,
        related_name='variants',
        help_text='Combo that this variant is an instance of',
        editable=False)
    status = models.CharField(choices=Status.choices, default=Status.NEW, help_text='Variant status for editors', max_length=2)
    mana_needed = models.CharField(blank=True, max_length=200, default='', help_text='Mana needed for this combo. Use the {1}{W}{U}{B}{R}{G}{B/P}... format.', validators=[MANA_VALIDATOR])
    mana_value_needed = models.IntegerField(editable=False, default=0, help_text='Mana value needed for this combo. Calculated from mana_needed.')
    other_prerequisites = models.TextField(blank=True, default='', help_text='Other prerequisites for this variant.', validators=TEXT_VALIDATORS)
    description = models.TextField(blank=True, help_text='Long description, in steps', validators=TEXT_VALIDATORS)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    generated_by = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, editable=False, help_text='Job that generated this variant', related_name='variants')

    class Meta:
        ordering = ['-status', '-created']
        verbose_name = 'variant'
        verbose_name_plural = 'variants'

    def cards(self):
        return self.uses.order_by('cardinvariant')

    def templates(self):
        return self.requires.order_by('templateinvariant')

    def __str__(self):
        if self.pk is None:
            return f'New variant with unique id <{self.id}>'
        produces = list(self.produces.all()[:4])
        return recipe([str(card) for card in self.cards()] + [str(template) for template in self.templates()], [str(feature) for feature in produces])

    def pre_save(self):
        self.mana_value_needed = mana_value(self.mana_needed)


class CardInVariant(IngredientInCombination):
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.card} in {self.variant.pk}'

    class Meta(IngredientInCombination.Meta):
        unique_together = [('card', 'variant')]


class TemplateInVariant(IngredientInCombination):
    template = models.ForeignKey(to=Template, on_delete=models.CASCADE)
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.template} in {self.variant.pk}'

    class Meta(IngredientInCombination.Meta):
        unique_together = [('template', 'variant')]
