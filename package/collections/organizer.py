
def get_words():
    with open('learnersdict.txt', 'r') as f:
        words_list = f.readlines()

    words_set = set()

    for w in words_list:
        word = w[:-1]
        words_set.add(word)

    new_words_list = sorted(words_set)

    return new_words_list