from .globals import inverted_index, docs_vec_length
from .tokenizer import *
from typing import List, Tuple, Dict
from math import sqrt
from .tfidf import *
import pdb
import heapq


def one_word_query(param: str) -> Dict[str, List[int]]:
    r = inverted_index.get(param)
    if r:
        return r
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


def one_word_query_scored(param: str) -> Dict[str, int]:
    r = one_word_query(param)
    s = tfidf(r)
    return s


def multi_word_query_scored(param: str, k: int) -> Dict[str, int]:
    result = {}
    tokens = tokenize(param)
#    params = punctuation_remover(params)
#    params = persian_number_remover(params)
#    params = english_number_remover(params)
#    tokens = params.split()
#    tokens = remove_nonverbal(tokens)
#    tokens = [remove_verb_prefix_postfix(token) for token in tokens]
#    tokens = remove_verbal(tokens)
    query_size = sqrt(doc_vec_len(tokens))
    for token in tokens:
        r = one_word_query_scored(token[0])
        for (key, value) in r.items():
            score = value * ((len(token) - 1) / sqrt(query_size))
            if result.get(key):
                result[key] += score
            else:
                result[key] = score
    h = list(result.items())
    h = [i[::-1] for i in h]
    heapq.heapify(h)
    return heapq.nlargest(k, h)




