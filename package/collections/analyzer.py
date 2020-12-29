import organizer as org

words_list = org.get_words()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

clusters = {}
letter_type = ''
prev_letter = ''
prev_letter_type = ''

for word in words_list:
    for l in range(len(word)):
        if word[l] in vowels:
            letter_type = 'vowel'
        else:
            letter_type = 'consonant'
        
        if l != 0:
            if letter_type == 'consonant' and prev_letter_type == 'consonant':
                cl = prev_letter + word[l]
                if cl in clusters:
                    clusters[cl] += 1
                else:
                    clusters[cl] = 1

        prev_letter = word[l]
        prev_letter_type = letter_type

print(dict(sorted(clusters.items(), key=lambda item: item[1])))
