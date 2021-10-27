import unittest
import random

from corpus_builder.builder_importer import from_text_file
from corpus_builder.builder import CorpusBuilder

class TestBuilderImporter(unittest.TestCase):
    def test_file_reader(self):
        builder = from_text_file('simple_domain.txt')
        self.assertIsInstance(builder, CorpusBuilder)

    def test_simple_sentence_generation(self):
        builder = from_text_file('simple_domain.txt')
        sentence, annotations = builder.create_sentence()
        self.assertIsInstance(sentence, str)
        self.assertIsInstance(annotations, dict)

    def test_simple_classification(self):
        builder = from_text_file('simple_domain.txt')
        sentence, annotations = builder.create_sentence()
        self.assertIn(annotations['<S>'], ['label_A', 'label_B'])

