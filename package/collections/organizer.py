import os
import unidecode

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


    def get_words_from_txt(self, path, code):
        dirname = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        print(dirname)
        filename = dirname + path
        print(filename)

        with open(filename, 'r') as f:
            lines = f.readlines()
        
        num_lines = 0

        items = set()

        for l in lines:
            l_string = l.lstrip()
            if l_string.startswith(code):
                item = l_string[7:42]
                if not item.startswith('.'):
                    item = item.rstrip().replace(',', '').replace('/', ' ').split()
                    for i in item:
                        decoded_item = unidecode.unidecode(i)
                        items.add(decoded_item)
        
        print(sorted(items))
        print('num lines: ', len(items))
