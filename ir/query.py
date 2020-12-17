from .globals import inverted_index
from .tokenizer import *
import pdb

def one_word_query(param: str):
    r = inverted_index.get(param)
    if r:
        return r
    print('Nothing found')
    return {}


def multi_words_query(params: str):
    result = {}

    params = punctuation_remover(params)
    params = persian_number_remover(params)
    params = english_number_remover(params)
    tokens = params.split()
    tokens = remove_nonverbal(tokens)
    tokens = [remove_verb_prefix_postfix(token) for token in tokens]
    tokens = remove_verbal(tokens)

    for token in tokens:
        r = one_word_query(token)
        for (doc, _) in r.items():
            if result.get(doc):
                result[doc] += 1
            else:
                result[doc] = 1

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

