#coding=utf-8
#Named Entity Recognizer
import nltk
from nltk.chunk import conlltags2tree, tree2conlltags

f = open('texto.txt', 'r')
text = f.read()

text = text.decode('ascii')

text_sentences = nltk.sent_tokenize(text)

tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in text_sentences]

tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

# chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

# def extract_entity_names(t):
#     entity_names = []

#     if hasattr(t, 'label') and t.label:

#         if t.label() == 'NE':
#             entity_names.append(' '.join([child[0] for child in t]))
#         else:
#             for child in t:
#                 entity_names.extend(extract_entity_names(child))

#     return entity_names

# entity_names = []
# for tree in chunked_sentences:
#     # Print results per sentence
#     print (extract_entity_names(tree))

#     entity_names.extend(extract_entity_names(tree))

p = "PERSON"
person_list = []

for x in tagged_sentences:
    test_part  = nltk.ne_chunk(x)
    print(test_part)