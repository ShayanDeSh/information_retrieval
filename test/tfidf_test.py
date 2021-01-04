import pytest
from ir.tfidf import *


@pytest.fixture
def index():
    d = {
        "1.txt": [1, 2, 3],
        "2.txt": [1, 2, 3, 4, 5 ,6],
        "3.txt": [1, 2, 3, 4, 5]
        }
    return d


def test_tf(index):
    t = tf(index)
    assert t == {
        "1.txt": 3,
        "2.txt": 6,
        "3.txt": 5
    }
