from string import punctuation
from typing import List, Tuple
from math import sqrt
from .helper import timer, verbal, nonverbal
from .globals import inverted_index, docs_vec_length
from .tfidf import *
import pdb

def create_index(doc_name: str, text: str):
    global inverted_index
    tokens = tokenize(text)
    vec_len = doc_vec_len(tokens)
    docs_vec_length[doc_name] = vec_len
    for token in tokens:
        name = token[0]
        if not inverted_index.get(name):
            index = {}
            index[doc_name] = list(token[1:])
            inverted_index[name] = index
        else:
            index = inverted_index[name]
            index[doc_name] = list(token[1:])


def tokenize(text: str) -> List[Tuple[str, ...]]:
    text = punctuation_remover(text)
    text = persian_number_remover(text)
    text = english_number_remover(text)
    tokens = text.split()
    tokens = remove_nonverbal(tokens)
    tokens = [remove_verb_prefix_postfix(token) for token in tokens]
    tokens = remove_verbal(tokens)
    tokens = [remove_noun_postfix(token) for token in tokens]
    tokens = positioner(tokens)
    tokens = sort_tuples(tokens)
    tokens = merge_duplicates(tokens)
    return tokens


def punctuation_remover(text: str) -> str:
    punc = punctuation + '\u200c' + '\u200b' + '،' + '؛'
    text = text.translate(str.maketrans('', '', punc))
    return text


def persian_number_remover(text: str) -> str:
    numbers = '۰۱۲۳۴۵۶۷۸۹١'
    text = text.translate(str.maketrans('', '', numbers))
    return text


def english_number_remover(text: str) -> str:
    numbers = '1234567890'
    text = text.translate(str.maketrans('', '', numbers))
    return text


def remove_nonverbal(tokens: List[str]) -> List[str]:
    r = [token for token in tokens if token not in nonverbal]
    return r


def remove_verbal(tokens: List[str]) -> List[str]:
    r = [token for token in tokens if token not in verbal]
    return r


def remove_verb_prefix_postfix(verb: str):
    _verb = remove_verb_prefix(verb)
    _verb = remove_verb_postfix(_verb)
    if _verb in verbal:
        return _verb
    return verb


def remove_verb_prefix(verb: str) -> str:
    if verb[0:2] == "می":
        verb = verb[2:]
    elif verb[0:2] == "ب":
        verb = verb[1:]
    return verb


def remove_verb_postfix(verb: str) -> str:
    if verb.endswith("ند"):
        verb = verb[0:-2]
    elif verb.endswith("ید"):
        verb = verb[0:-2]
    elif verb.endswith("یم"):
        verb = verb[0:-2]
    elif verb.endswith("م"):
        verb = verb[0:-1]
    elif verb.endswith("ی"):
        verb = verb[0:-1]
    elif verb.endswith("د"):
        verb = verb[0:-1]
    return verb


def remove_noun_postfix(noun: str) -> str:
    _noun = remove_noun_relative_postfix(noun)
    _noun = remove_noun_comparative_postfix(_noun)
    return _noun


def remove_noun_relative_postfix(noun: str) -> str:
    if noun.endswith("ی"):
        noun = noun[0:-1]
    return noun


def remove_noun_comparative_postfix(noun: str) -> str:
    if noun.endswith("تر"):
        noun = noun[0:-2]
    elif noun.endswith("ترین"):
        noun = noun[0:-4]
    return noun


def positioner(tokens: List[str]) -> List[Tuple[str, ...]]:
    r = []
    for (i, token) in enumerate(tokens):
        r.append((token, i))
    return r


def sort_tuples(tuples: List[Tuple[str, ...]]) -> List[Tuple[str, ...]]:
    return sorted(tuples)


def merge_duplicates(tokens:
        List[Tuple[str, ...]]) -> List[Tuple[str, ...]]:
    r = [tokens.pop(0)]
    for token in tokens:
        if token[0] == r[-1][0]:
            r[-1] += token[1:]
        else:
            r.append(token)
    return r


def doc_vec_len(tokens: List[Tuple[str, ...]]) -> int:
    r = 0 
    for token in tokens:
        r += (len(token) - 1) ** 2
    return r


def champions_list(d, k):
    result = {}
    for (key, value) in d:
        r = tf(d)
        r = dict(sorted(r.items(), key=lambda item: item[1], reverse=True)[0:k])
        result[key] = r
    return result


