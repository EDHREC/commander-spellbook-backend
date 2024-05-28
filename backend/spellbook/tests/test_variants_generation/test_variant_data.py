from spellbook.tests.abstract_test import AbstractTestCaseWithSeeding
from spellbook.variants.variant_data import Data, debug_queries
from spellbook.models import Variant, Combo, Feature, Card, Template, id_from_cards_and_templates_ids
from multiset import FrozenMultiset


class VariantDataTests(AbstractTestCaseWithSeeding):
    def setUp(self):
        super().setUp()
        super().generate_variants()

    def test_combos(self):
        data = Data()
        query = Combo.objects.filter(status__in=(Combo.Status.GENERATOR, Combo.Status.UTILITY))
        self.assertEqual(len(data.combos), query.count())
        self.assertDictEqual(data.id_to_combo, {c.id: c for c in query.all()})
        self.assertEqual(set(c.id for c in data.generator_combos), set(Combo.objects.filter(status=Combo.Status.GENERATOR).values_list('id', flat=True)))
        self.assertDictEqual({k: data.combo_to_cards[k] for k in query.values_list('id', flat=True)}, {combo.id: list(combo.cardincombo_set.all()) for combo in query.all()})
        self.assertDictEqual({k: data.combo_to_templates[k] for k in query.values_list('id', flat=True)}, {combo.id: list(combo.templateincombo_set.all()) for combo in query.all()})
        self.assertDictEqual({k: data.combo_to_produced_features[k] for k in query.values_list('id', flat=True)}, {combo.id: list(combo.featureproducedincombo_set.all()) for combo in query.all()})
        self.assertDictEqual({k: data.combo_to_needed_features[k] for k in query.values_list('id', flat=True)}, {combo.id: list(combo.featureneededincombo_set.all()) for combo in query.all()})
        self.assertDictEqual({k: data.combo_to_removed_features[k] for k in query.values_list('id', flat=True)}, {combo.id: list(combo.featureremovedincombo_set.all()) for combo in query.all()})

    def test_cards(self):
        data = Data()
        self.assertEqual(set(c.id for c in data.cards), set(Card.objects.values_list('id', flat=True)))
        self.assertDictEqual({k: data.card_to_features[k] for k in Card.objects.values_list('id', flat=True)}, {card.id: list(card.featureofcard_set.all()) for card in Card.objects.all()})
        self.assertDictEqual(data.id_to_card, {c.id: c for c in Card.objects.all()})

    def test_templates(self):
        data = Data()
        self.assertEqual(set(t.id for t in data.templates), set(Template.objects.values_list('id', flat=True)))
        self.assertDictEqual(data.id_to_template, {t.id: t for t in Template.objects.all()})

    def test_features(self):
        data = Data()
        self.assertEqual(set(f.id for f in data.features), set(Feature.objects.values_list('id', flat=True)))
        self.assertEqual(data.id_to_feature, {f.id: f for f in Feature.objects.all()})

    def test_utility_features_ids(self):
        data = Data()
        self.assertSetEqual(data.utility_features_ids, set(Feature.objects.filter(utility=True).values_list('id', flat=True)))

    def test_variants(self):
        data = Data()
        self.assertEqual(set(v.id for v in data.variants), set(Variant.objects.values_list('id', flat=True)))
        self.assertSetEqual(
            set(id_from_cards_and_templates_ids(v[0], v[1]) for v in data.not_working_variants),
            set(Variant.objects.filter(status=Variant.Status.NOT_WORKING).values_list('id', flat=True)),
        )
        self.assertDictEqual(data.id_to_variant, {v.id: v for v in Variant.objects.all()})
        self.assertDictEqual(data.card_in_variant, {v.id: list(v.cardinvariant_set.all()) for v in Variant.objects.all()})
        self.assertDictEqual(data.template_in_variant, {v.id: list(v.templateinvariant_set.all()) for v in Variant.objects.all()})
        self.assertDictEqual(data.variant_to_of, {v.id: {i.combo.id: i for i in v.variantofcombo_set.all()} for v in Variant.objects.all()})
        self.assertDictEqual(data.variant_to_includes, {v.id: {i.combo.id: i for i in v.variantincludescombo_set.all()} for v in Variant.objects.all()})
        self.assertDictEqual(data.variant_to_produces, {v.id: {i.feature.id: i for i in v.featureproducedbyvariant_set.all()} for v in Variant.objects.all()})

    def test_not_working_variants(self):
        super().generate_variants()
        self.v1_id = id_from_cards_and_templates_ids([self.c8_id, self.c1_id], [self.t1_id])
        v1: Variant = Variant.objects.get(id=self.v1_id)
        v1.status = Variant.Status.NOT_WORKING
        v1.save()
        data = Data()
        self.assertSetEqual(set(data.not_working_variants), {(FrozenMultiset([self.c8_id, self.c1_id]), FrozenMultiset([self.t1_id]))})
        super().generate_variants()
        data = Data()
        self.assertSetEqual(set(data.not_working_variants), {(FrozenMultiset([self.c8_id, self.c1_id]), FrozenMultiset())})

    def test_card_variant_dict(self):
        data = Data()
        for card_id, variant_id in data.card_variant_dict:
            self.assertIn(card_id, set(data.id_to_variant[variant_id].uses.all().values_list('id', flat=True)))

    def test_template_variant_dict(self):
        data = Data()
        for template_id, variant_id in data.template_variant_dict:
            self.assertIn(template_id, set(data.id_to_variant[variant_id].requires.all().values_list('id', flat=True)))

    def test_debug_queries(self):
        with self.settings(DEBUG=True):
            q = debug_queries()
            Variant.objects.all().count()
            self.assertEqual(debug_queries() - q, 1)

    def test_number_of_queries(self):
        with self.settings(DEBUG=True):
            q = debug_queries()
            Data()
            self.assertEqual(debug_queries() - q, 20)
        with self.settings(DEBUG=True):
            q = debug_queries()
            Data(
                cards=[],
                templates=[],
                combos=[],
                features=[],
                variants=[],
            )
            self.assertEqual(debug_queries() - q, 0)
