def break_words(stuff):
    """This function will break up words for us."""
    return stuff.split(' ')

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after poppin it off."""
    print words.pop(0)

def print_last_word(words):
    """Print the last word after popping it off."""
    print words.pop(-1)

def sort_sentende(sentence):
    """Takes in a full sentence and return the sorted words."""
    return sort_words(break_words(sentence))

def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
