import organizer as org

words_list = org.get_words()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

cons_clusters = {}
vowel_clusters = {}
letter_type = ''
prev_letter = ''
prev_letter_type = ''

for word in words_list:
    for l in range(len(word)):
        if word[l] in vowels:
            letter_type = 'vowel'
        elif word[l] in consonants:
            letter_type = 'consonant'
        else:
            letter_type = 'other'
        
        if l != 0:
            if letter_type == 'consonant' and prev_letter_type == 'consonant':
                cl = prev_letter + word[l]
                if cl in cons_clusters:
                    cons_clusters[cl] += 1
                else:
                    cons_clusters[cl] = 1
            
            if letter_type == 'vowel' and prev_letter_type == 'vowel':
                cl = prev_letter + word[l]
                if cl in vowel_clusters:
                    vowel_clusters[cl] += 1
                else:
                    vowel_clusters[cl] = 1

        prev_letter = word[l]
        prev_letter_type = letter_type

total_cons = 0
total_vowels = 0

for c in cons_clusters:
    total_cons += cons_clusters[c]
for c in cons_clusters:
    cons_clusters[c] = round(cons_clusters[c]/total_cons*100, 5)

for v in vowel_clusters:
    total_vowels += vowel_clusters[v]
for v in vowel_clusters:
    vowel_clusters[v] = round(vowel_clusters[v]/total_vowels*100, 5)

print(dict(sorted(cons_clusters.items(), key=lambda item: item[1], reverse=True)))
print(dict(sorted(vowel_clusters.items(), key=lambda item: item[1], reverse=True)))
