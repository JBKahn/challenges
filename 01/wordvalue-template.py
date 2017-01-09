from operator import itemgetter

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open("./" + DICTIONARY) as f:
        return f.readlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(map(lambda letter: LETTER_SCORES[letter], word))

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()

    return max(map(calc_word_value, word_list))

if __name__ == "__main__":
    pass # run unittests to validate
