from string import punctuation
from typing import List, Tuple
from .helper import timer, verbal, nonverbal


inverted_index = {}


def create_index(doc_name: str, text: str):
    global inverted_index
    tokens = tokenize(text)
    for token in tokens:
        name = token[0]
        if not inverted_index.get(name):
            index = {}
            index[doc_name] = list(token[1:])
            inverted_index[name] = index
        else:
            index = inverted_index[name]
            index[doc_name] = list(token[1:])


def tokenize(text: str) -> List[str]:
    text = punctuation_remover(text)
    text = number_remover(text)
    tokens = text.split()
    tokens = remove_nonverbal(tokens)
    tokens = remove_verbal(tokens)
    tokens = positioner(tokens)
    tokens = sort_tuples(tokens)
    tokens = merge_duplicates(tokens)
    return tokens


def punctuation_remover(text: str) -> str:
    punc = punctuation + '\u200c' + '\u200b' + '،'
    text = text.translate(str.maketrans('', '', punc))
    return text


def number_remover(text: str) -> str:
    numbers = '۱۲۳۴۵۶۷۸۹١'
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
    _verb = remove_verb_postfix(verb)
    if _verb in verbal:
        return _verb


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


