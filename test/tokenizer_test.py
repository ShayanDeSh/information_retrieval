import pytest
from ir.tokenizer import tokenize

@pytest.fixture
def docs():
    from os import listdir

    docs = []
    for doc in listdir('./test/sampleDoc'):
        with open("./test/sampleDoc/{}".format(doc)) as doc:
            docs.append(doc.read())
    return docs


def test_tokenize(docs):
    for a in tokenize(docs[0]):
        print(a)
    assert False
