from corpus_builder.rule import Rule
from corpus_builder.grammar import Grammar
from corpus_builder.builder import CorpusBuilder

root_rule = Rule('<S>', ('<A>', '<B>'))
a_rule = Rule('<A>', ['a', '<B>'])
b_rule = Rule('<B>', ('<A>', 'b', '<C>'))
c_rule = Rule('<C>', 'c')

rule_set = [root_rule, a_rule, b_rule, c_rule]

grammar = Grammar(rule_set, '<S>')

builder = CorpusBuilder(grammar, {'<S>': ['A', 'B']}, {'<C>': 'C'})
print(builder.create_sentence())
print(builder.create_corpus(5, 0))