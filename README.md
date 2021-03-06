# Corpus Constructor

Tool for semi-automatic corpus construction for training NLP models.
This project allows for a definition of a domain corpus by using a
context-free grammar in the BNF form. This grammar is used to produce
sample sentences belonging to this defined language. That are later
expanded by textual data augmentation to form a specific domain
corpus that could be used to train machine learning models such as
intent classifier and NER.

## Installation

Curenttly the only instalation method is by clonning this repo and
installing dependencies manually.

## Usage

A simple example with a syntetic language is as follows:

```python
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
```

A more complex example with natural language in the AskUbuntu corpus
domain is in the [ask_ubuntu.py](src/ask_ubuntu.py) file.

It is also possible to create a grammar from a text file in [this](src/simple_domain.txt) format. Then create the corpus builder as use it as follows

```python
from corpus_builder.builder_importer import from_text_file

builder = from_text_file('simple_domain.txt')
print(builder.create_sentence())
print(builder.create_corpus(5, 0))
```

Or by using the command line utility

```bash
python -m corpus_builder --input simple_domain.txt -n 5
```
