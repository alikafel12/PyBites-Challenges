from data import DICTIONARY, LETTER_SCORES

class word_object:

    def __init__(self, word):
        self.word = word
        self.value = calc_word_value(word)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

def load_words():
    """Load dictionary into a list and return list"""
    dict = DICTIONARY
    file = open(dict, 'r')
    words = file.read().splitlines()
    file.close()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        if letter.upper() not in LETTER_SCORES:
            continue
        word_value += LETTER_SCORES[letter.upper()]
    return word_value

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = word_object('hold')
    max_word.value = 0
    for word in words:
        curr_word = word_object(word)
        if curr_word > max_word:
            max_word = curr_word
    return max_word.word


if __name__ == "__main__":
    pass
