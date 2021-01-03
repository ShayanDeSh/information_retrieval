from .globals import inverted_index, docs_vec_length
from .tokenizer import *
from typing import List, Tuple
from math import log
import pdb


def one_word_query(param: str) -> dict[str, List[int]]:
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


def one_word_query_scored(param: str):
    r = one_word_query(param)
    s = tfidf(r)
    return s


def multi_word_query_scored(param: str):
    result = {}
    params = punctuation_remover(params)
    params = persian_number_remover(params)
    params = english_number_remover(params)
    tokens = params.split()
    tokens = remove_nonverbal(tokens)
    tokens = [remove_verb_prefix_postfix(token) for token in tokens]
    tokens = remove_verbal(tokens)
    for token in tokens:
        r = one_word_query_scored(token)
        for (key, value) in r.items():
            result[]


def tf(d: dict[str, List[int]]) -> dict[str, int]:
    r = {}
    for (key, value) in d.items():
        r[key] = len(value)
    r = normalize_tf(r)
    return r


def normalize_tf(d: dict[str, int]) -> dict[str, int]:
    r = {}
    for (key, value) in d.items():
        r[key] = log(value / docs_vec_length[key] + 1)
    return r


def idf(d: dict[str, int]) -> float:
    return log(len(docs_vec_length) / len(d))


def tfidf(d: dict[str, int]) -> dict[str, int]:
    t = tf(d)
    i = idf(r)
    ti = {}
    for (key, value) in t:
        ti[key] = value * i
    return ti


