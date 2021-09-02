import unittest
import random

from corpus_builder.text_augmentation import *

class TestEDA(unittest.TestCase):

    def setUp(self):
        self.sentence = 'the quick brown fox jumps over the lazy dog'.split()
        random.seed(1)

    def test_default_stopwords(self):
        stopwords = get_stopwords()
        self.assertIn('the', stopwords, 'Default stopwords english should be english')

    def test_synonym_replace(self):
        new_sentence = synonym_replace(self.sentence, 1)
        self.assertEqual(len(new_sentence), len(self.sentence), 'Synonym replacement should produce sentence with the same length')

    def test_random_insertion(self):
        new_sentence = random_insertion(self.sentence, 1)
        self.assertEqual(len(new_sentence), len(self.sentence)+1, 'Random insertion should add a word to the sentence')

    def test_random_swap(self):
        new_sentence = random_swap(self.sentence, 1)
        self.assertEqual(len(new_sentence), len(self.sentence), 'Random swap should mantain the number of words in the sentence')

    def test_random_deletion(self):
        new_sentence = random_deletion(self.sentence, 0.1)
        self.assertTrue(len(new_sentence) < len(self.sentence), f'Random deletion should reduce the number of words in the sentence ({len(new_sentence)} < {len(self.sentence)})')

    def test_eda(self):
        extra_sentences = eda(' '.join(self.sentence))
        self.assertEqual(len(extra_sentences), 10)