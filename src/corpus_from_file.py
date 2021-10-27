from corpus_builder.builder_importer import from_text_file

builder = from_text_file('simple_domain.txt')
print(builder.create_sentence())
print(builder.create_corpus(5, 0))