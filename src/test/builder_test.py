import unittest
import random

from corpus_builder.grammar import Grammar
from corpus_builder.rule import Rule
from corpus_builder.builder import CorpusBuilder

class TestCorpusBuilder(unittest.TestCase):

    def setUp(self):
        self.grammar = Grammar([
            Rule('<S>', ('<A>', '<B>', '<C>')),
            Rule('<A>', ['<D>', 'a']),
            Rule('<B>', 'b'),
            Rule('<C>', ['<D>', '<E>']),
            Rule('<D>', 'd'),
            Rule('<E>', 'e'),
        ], '<S>')
        self.classes_labels = {
            '<S>': ['label_A', 'label_B', 'label_C']
        }
        self.entities_labels = {
            '<D>': 'entity_D',
            '<E>': 'entity_E'
        }
        self.builder = CorpusBuilder(self.grammar, self.classes_labels, self.entities_labels)

    def test_simple_sentence_generation(self):
        sentence, annotations = self.builder.create_sentence()
        self.assertIsInstance(sentence, str)
        self.assertIsInstance(annotations, dict)

    def test_simple_classification(self):
        sentence, annotations = self.builder.create_sentence()
        self.assertIn(annotations['<S>'], self.classes_labels['<S>'])

    def test_simple_entity(self):
        random.seed(5)
        sentence, annotations = self.builder.create_sentence()
        value, label = annotations['entities'][0]
        self.assertEqual(value, 'd')
        self.assertEqual(label, 'entity_D')

    def test_simple_corpus(self):
        corpus = self.builder.create_corpus(10, 0)
        self.assertIsInstance(corpus, list)
        self.assertIsInstance(corpus[0], tuple)
        self.assertIsInstance(corpus[0][0], str)
        self.assertIsInstance(corpus[0][1], dict)
