from string import punctuation
from .helper import timer

def tokenize(text):
    return text\
            .punctuation_remover()\
            .split()

@timer
def punctuation_remover(text):
    text = text.translate(str.maketrans('', '', punctuation))
    return text
