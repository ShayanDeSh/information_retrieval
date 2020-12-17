from .globals import inverted_index

def one_word_query(param: str):
    r = inverted_index.get(param)
    if r:
        return r
    print('Nothing found')
    return None


def multi_word_query(param: str):
    r = inverted_index.get(param)
    if r:
        return r
    print('Nothing found')
    return None
