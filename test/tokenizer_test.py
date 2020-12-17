import pytest
from ir.tokenizer import *
import ujson
from ir.query import *


@pytest.fixture
def docs():
    from os import listdir
    docs = []
    for doc in listdir('./test/sampleDoc'):
        with open("./test/sampleDoc/{}".format(doc)) as doc_file:
            docs.append((doc, doc_file.read()))
    return docs


def test_punctuation_remover():
    import string

    result = punctuation_remover(string.punctuation)
    assert result == ''


def test_persian_number_remover():
    result = persian_number_remover('۱۲۳۴۵۶۷۸۹')
    assert result == ''
    

def test_persian_number_remover():
    result = english_number_remover('1234567890')
    assert result == ''


def test_positioner():
    result = positioner(['a', 'b', 'c'])
    assert result == [('a', 0), ('b', 1), ('c', 2)]


def test_sort_tuples():
    result = sort_tuples([('f', 1), ('b', 0), ('d', 5), ('d', 6)])
    assert result == [('b', 0), ('d', 5), ('d', 6), ('f', 1)]


def test_merge_duplicates():
    result = merge_duplicates([('b', 0), ('b', 2), ('d', 5), ('d', 7),
        ('d', 9), ('f', 1)])
    assert result == [('b', 0, 2), ('d', 5, 7, 9), ('f', 1)]


def test_tokenize(docs):
    result = tokenize(docs[0][1])


def test_create_index(docs):
    for (name, doc) in docs:
        create_index(name, doc)
    with open('index.json', "w") as json_file:
        ujson.dump(inverted_index, json_file, indent=4, ensure_ascii=False)
    assert False


