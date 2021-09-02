import unittest

from corpus_builder.grammar import Grammar
from corpus_builder.rule import Rule
from corpus_builder.exceptions import RuleNotFoundException

class TestGrammar(unittest.TestCase):

    def test_find_rule_success(self):
        rule = Rule('<A>', 'a')
        grammar = Grammar([rule], '<A>')
        self.assertEqual(grammar.get_rule('<A>'), rule)

    def test_find_rule_unccess(self):
        rule = Rule('<A>', 'a')
        grammar = Grammar([rule], '<A>')
        with self.assertRaises(RuleNotFoundException):
            grammar.get_rule('<B>')