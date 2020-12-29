import organizer as org

words_list = org.get_words()

vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

letters = {}
cons = {}
vowels = {}
cons_clusters = {}
vowel_clusters = {}

letter_type = ''
prev_letter = ''
prev_letter_type = ''

for word in words_list:
    for l in range(len(word)):
        if word[l] in vowels_list:
            letter_type = 'vowel'
            if word[l] in vowels:
                vowels[word[l]] += 1
            else:
                vowels[word[l]] = 1
        elif word[l] in consonants_list:
            letter_type = 'consonant'
            if word[l] in cons:
                cons[word[l]] += 1
            else:
                cons[word[l]] = 1
        else:
            letter_type = 'other'

        if letter_type != 'other':
            if word[l] in letters:
                letters[word[l]] += 1
            else:
                letters[word[l]] = 1
        
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

total_letters = 0
total_cons = 0
total_vowels = 0
total_cons_cl = 0
total_vowels_cl = 0

for l in letters:
    total_letters += letters[l]
for l in letters:
    letters[l] = round(letters[l]/total_letters*100, 5)

for c in cons:
    total_cons += cons[c]
for c in cons:
    cons[c] = round(cons[c]/total_cons*100, 5)

for v in vowels:
    total_vowels += vowels[v]
for v in vowels:
    vowels[v] = round(vowels[v]/total_vowels*100, 5)

for c in cons_clusters:
    total_cons_cl += cons_clusters[c]
for c in cons_clusters:
    cons_clusters[c] = round(cons_clusters[c]/total_cons_cl*100, 5)

for v in vowel_clusters:
    total_vowels_cl += vowel_clusters[v]
for v in vowel_clusters:
    vowel_clusters[v] = round(vowel_clusters[v]/total_vowels_cl*100, 5)

print("Letters: ", dict(sorted(letters.items(), key=lambda item: item[1], reverse=True)))
print()
print("Consonants: ", dict(sorted(cons.items(), key=lambda item: item[1], reverse=True)))
print()
print("Vowels: ", dict(sorted(vowels.items(), key=lambda item: item[1], reverse=True)))
print()
print("Cons Clusters: ", dict(sorted(cons_clusters.items(), key=lambda item: item[1], reverse=True)))
print()
print("Vowel Clusters: ", dict(sorted(vowel_clusters.items(), key=lambda item: item[1], reverse=True)))
