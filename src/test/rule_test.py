import unittest

from corpus_builder.rule import Rule
from corpus_builder.exceptions import InvalidRuleException

class TestRule(unittest.TestCase):
    
    def test_direct_string_rule(self):
        rule = Rule('<A>', 'a')
        result = rule.expand()
        self.assertEqual('a', result, 'Direct string rule should expand to the string')

    def test_tuple_rule(self):
        rule = Rule('<A>', ('a', 'b', 'c'))
        result = rule.expand()
        self.assertIn(result, ('a', 'b', 'c'), 'Tuple rule should randomply choose one of its members')

    def test_list_rule(self):
        rule = Rule('<A>', ['a', 'b', 'c'])
        result = rule.expand()
        self.assertEqual('a b c', result, 'List rule should concatenate its members')

    def test_invalid_rule(self):
        rule = Rule('<A>', None)
        with self.assertRaises(InvalidRuleException):
            rule.expand()