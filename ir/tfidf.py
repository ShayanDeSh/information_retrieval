from math import log, sqrt
from typing import List, Tuple, Dict
from .globals import inverted_index, docs_vec_length
import pdb


def tf(d: Dict[str, List[int]]) -> Dict[str, int]:
    r = {}
    for (key, value) in d.items():
        r[key] = len(value)
    return r


def normalize_tf(d: Dict[str, int]) -> Dict[str, int]:
    r = {}
    for (key, value) in d.items():
        r[key] = log(value / sqrt(docs_vec_length[key]) + 1)
    return r


def idf(d: Dict[str, int]) -> float:
    return log(len(docs_vec_length) / len(d))


def tfidf(d: Dict[str, List[int]]) -> Dict[str, int]:
    t = tf(d)
    t = normalize_tf(t)
    i = idf(t)
    print(i)
    ti = {}
    for (key, value) in t.items():
        ti[key] = value * i
    return ti
