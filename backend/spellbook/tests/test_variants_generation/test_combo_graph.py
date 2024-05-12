from multiset import FrozenMultiset
from spellbook.models import Combo
from spellbook.variants.variant_data import Data
from spellbook.variants.combo_graph import Graph, VariantIngredients
from spellbook.tests.abstract_test import AbstractTestCaseWithSeeding, AbstractTestCase


class ComboGraphTest(AbstractTestCaseWithSeeding):
    def test_empty_graph(self):
        Combo.objects.exclude(id=self.b2_id).delete()
        combo_graph = Graph(Data())
        self.assertCountEqual(combo_graph.variants(self.b2_id), [])

    def test_graph(self):
        combo_graph = Graph(Data())
        variants = list(combo_graph.variants(self.b2_id))
        self.assertEqual(variants, list(combo_graph.variants(self.b2_id)))
        self.assertEqual(len(variants), 3)

    def test_variant_limit(self):
        combo_graph = Graph(Data(), log=lambda _: None, variant_limit=0)
        self.assertRaises(Graph.GraphError, lambda: combo_graph.variants(self.b2_id))
        combo_graph = Graph(Data(), log=lambda _: None, variant_limit=1)
        self.assertRaises(Graph.GraphError, lambda: combo_graph.variants(self.b2_id))
        combo_graph = Graph(Data(), log=lambda _: None, variant_limit=20)
        self.assertEqual(len(list(combo_graph.variants(self.b2_id))), 3)

    def test_default_log(self):
        def test():
            combo_graph = Graph(Data(), variant_limit=0)
            list(combo_graph.variants(self.b2_id))
        self.assertRaises(Exception, test)

    def test_card_limit(self):
        self.maxDiff = None
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=0)
        self.assertCountEqual(combo_graph.variants(self.b2_id), [])
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=1)
        self.assertCountEqual(combo_graph.variants(self.b2_id), [])
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=2)
        self.assertCountEqual(combo_graph.variants(self.b2_id), [])
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=3)
        self.assertEqual(len(list(combo_graph.variants(self.b2_id))), 1)
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=4)
        self.assertEqual(len(list(combo_graph.variants(self.b2_id))), 2)
        combo_graph = Graph(Data(), log=lambda _: None, card_limit=5)
        self.assertEqual(len(list(combo_graph.variants(self.b2_id))), 3)

    def test_replacements(self):
        data = Data()
        combo_graph = Graph(data=data)
        variants = list(combo_graph.variants(self.b2_id))
        for variant in variants:
            card_ids = {c for c in variant.cards}
            template_ids = {t for t in variant.templates}
            replacements = variant.replacements
            feature_needed_by_combos = {f.id for f in data.id_to_combo[self.b2_id].features_needed()}  # type: set[int]
            self.assertTrue(set(replacements.keys()).issuperset(feature_needed_by_combos))
            for replacement_values in replacements.values():
                self.assertGreaterEqual(len(replacement_values), 1)
                for replacement_value in replacement_values:
                    cards = replacement_value.cards
                    templates = replacement_value.templates
                    replacement_card_ids = {c for c in cards}
                    replacement_template_ids = {t for t in templates}
                    self.assertTrue(card_ids.issuperset(replacement_card_ids))
                    self.assertTrue(template_ids.issuperset(replacement_template_ids))


class ComboGraphTestGeneration(AbstractTestCase):
    def test_one_card_combo(self):
        self.save_combo_model({
            ('A',): ('x',),
        })
        combo_graph = Graph(Data())
        variants = combo_graph.variants(1)
        self.assertEqual(len(list(variants)), 1)
        self.assertMultisetEqual(variants[0].cards, {1: 1})
        self.assertMultisetEqual(variants[0].templates, {})
        self.assertListEqual(sorted(variants[0].combos), [1])
        self.assertMultisetEqual(variants[0].features, {1: 1})
        self.assertMultisetEqual(variants[0].replacements, {1: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset())]})

    def test_two_one_card_combo(self):
        self.save_combo_model({
            ('A',): ('x',),
            ('B',): ('x',),
        })
        combo_graph = Graph(Data())
        variants = combo_graph.variants(1)
        self.assertEqual(len(list(variants)), 1)
        self.assertMultisetEqual(variants[0].cards, {1: 1})
        self.assertMultisetEqual(variants[0].templates, {})
        self.assertListEqual(sorted(variants[0].combos), [1])
        self.assertMultisetEqual(variants[0].features, {1: 1})
        self.assertMultisetEqual(variants[0].replacements, {1: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset())]})
        variants = combo_graph.variants(2)
        self.assertEqual(len(list(variants)), 1)
        self.assertMultisetEqual(variants[0].cards, {2: 1})
        self.assertMultisetEqual(variants[0].templates, {})
        self.assertListEqual(sorted(variants[0].combos), [2])
        self.assertMultisetEqual(variants[0].features, {1: 1})
        self.assertMultisetEqual(variants[0].replacements, {1: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())]})

    def test_card_plus_template(self):
        self.save_combo_model({
            ('A', 'T1'): ('x', 'y'),
        })
        combo_graph = Graph(Data())
        variants = combo_graph.variants(1)
        self.assertEqual(len(list(variants)), 1)
        self.assertMultisetEqual(variants[0].cards, {1: 1})
        self.assertMultisetEqual(variants[0].templates, {1: 1})
        self.assertListEqual(sorted(variants[0].combos), [1])
        self.assertMultisetEqual(variants[0].features, {1: 1, 2: 1})
        self.assertMultisetEqual(variants[0].replacements, {
            1: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset({1: 1}))],
            2: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset({1: 1}))],
        })

    def test_feature_replacement(self):
        self.save_combo_model({
            ('A',): ('x',),
            ('B',): ('x',),
            ('x',): ('y',),
        })
        combo_graph = Graph(Data())
        variants = combo_graph.variants(3)
        self.assertEqual(len(list(variants)), 2)
        variants.sort(key=lambda v: sorted(v.cards))
        self.assertMultisetEqual(variants[0].cards, {1: 1})
        self.assertMultisetEqual(variants[0].templates, {})
        self.assertListEqual(sorted(variants[0].combos), [1, 3])
        self.assertMultisetEqual(variants[0].features, {1: 1, 2: 1})
        self.assertMultisetEqual(variants[0].replacements, {
            1: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset())],
            2: [VariantIngredients(FrozenMultiset({1: 1}), FrozenMultiset())],
        })
        self.assertMultisetEqual(variants[1].cards, {2: 1})
        self.assertMultisetEqual(variants[1].templates, {})
        self.assertListEqual(sorted(variants[1].combos), [2, 3])
        self.assertMultisetEqual(variants[1].features, {1: 1, 2: 1})
        self.assertMultisetEqual(variants[1].replacements, {
            1: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
            2: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
        })

    def test_feature_replacement_chain(self):
        self.save_combo_model({
            ('A',): ('x',),
            ('B',): ('x',),
            ('x',): ('y',),
            ('y',): ('z',),
        })
        combo_graph = Graph(Data())
        variants_a = combo_graph.variants(4)
        variants_b = combo_graph.variants(3)
        variants_a.sort(key=lambda v: sorted(v.cards))
        variants_b.sort(key=lambda v: sorted(v.cards))
        self.assertEqual(variants_a, variants_b)
        self.assertMultisetEqual(variants_a[0].features, {1: 1, 2: 1, 3: 1})
        self.assertListEqual(sorted(variants_a[0].combos), [1, 3, 4])

    def test_feature_replacement_multiples_cards(self):
        self.save_combo_model({
            ('2 * A',): ('x',),
            ('B',): ('x',),
            ('x',): ('y',),
        })
        combo_graph = Graph(Data())
        with self.settings(SINGLETON_COMBO_MODE=False):
            variants = list(combo_graph.variants(3))
            self.assertEqual(len(variants), 2)
            variants.sort(key=lambda v: sorted(v.cards))
            self.assertMultisetEqual(variants[0].cards, {1: 2})
            self.assertMultisetEqual(variants[0].templates, {})
            self.assertMultisetEqual(variants[0].features, {1: 1, 2: 1})
            self.assertListEqual(sorted(variants[0].combos), [1, 3])
            self.assertMultisetEqual(variants[0].replacements, {
                1: [VariantIngredients(FrozenMultiset({1: 2}), FrozenMultiset())],
                2: [VariantIngredients(FrozenMultiset({1: 2}), FrozenMultiset())],
            })
            self.assertMultisetEqual(variants[1].cards, {2: 1})
            self.assertMultisetEqual(variants[1].templates, {})
            self.assertMultisetEqual(variants[1].features, {1: 1, 2: 1})
            self.assertListEqual(sorted(variants[1].combos), [2, 3])
            self.assertMultisetEqual(variants[1].replacements, {
                1: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
                2: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
            })
        combo_graph = Graph(Data())
        variants = list(combo_graph.variants(3))
        self.assertEqual(len(variants), 1)
        self.assertMultisetEqual(variants[0].cards, {2: 1})
        self.assertMultisetEqual(variants[0].templates, {})
        self.assertMultisetEqual(variants[0].features, {1: 1, 2: 1})
        self.assertListEqual(sorted(variants[0].combos), [2, 3])
        self.assertMultisetEqual(variants[0].replacements, {
            1: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
            2: [VariantIngredients(FrozenMultiset({2: 1}), FrozenMultiset())],
        })

    # TODO: more tests
