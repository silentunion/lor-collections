import os

class Collections():
    def get_words(self):
        with open('learnersdict.txt', 'r') as f:
            words_list = f.readlines()

        words_set = set()

        for w in words_list:
            word = w[:-1]
            words_set.add(word.lower())

        new_words_list = sorted(words_set)

        return new_words_list


    def get_words_from_txt(self, path):
        dirname = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        print(dirname)
        filename = dirname + path
        print(filename)

        with open(filename, 'r') as f:
            lines = f.readlines()
        
        num_lines = 0

        for l in lines:
            num_lines += 1
        
        print('num lines: ', num_lines)
