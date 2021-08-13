import generate_word as gw

word = []
failed_attempts = 0
last_word = []


def __main__():
    global word
    global failed_attempts
    global last_word
    word = list(gw.get_word())
    last_word = list("_"*len(word))


def replace(character, string):
    tuple_words = tuple(zip(string, last_word))
    word = [w if w == character else l for w, l in tuple_words]
    return word


def view(character):
    global last_word
    global failed_attempts
    new_word = replace(character, word)
    if last_word == new_word:
        failed_attempts += 1
        return last_word, True, failed_attempts
    else:
        last_word = new_word
        return last_word, False, failed_attempts



