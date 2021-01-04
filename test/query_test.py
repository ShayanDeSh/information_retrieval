from ir.query import *


def test_one_word_query():
    r = one_word_query('بیمار')
    assert r == {'2.txt': [41]}


def test_multi_words_query():
    r = multi_words_query('علیرضا منصوریان')
    assert r == {'1.txt': 2}
    r = multi_words_query('یبسش سیشب بشسیب شببشسی')
    assert r == {}
    r = multi_words_query('تراکتور قهرمان جام حذفی')
    print(r)


def test_one_word_query_scored():
    r = one_word_query_scored('بیمار')
    print(r)


def test_multi_words_query_scored():
    r = multi_word_query_scored('فوتبال ملی', 5)
    print(r)
