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

total_letters = 0
total_cons = 0
total_vowels = 0
total_cons_cl = 0
total_vowels_cl = 0

# Adds item to the specified dictionary
def add_item_to_dic(item, dic):
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

# Converts values added up to a percentile
def convert_to_percent(total, dic):
    for d in dic:
        total += dic[d]
    for d in dic:
        dic[d] = round(dic[d]/total*100, 5)


for word in words_list:
    for l in range(len(word)):
        if word[l] in vowels_list:
            letter_type = 'vowel'

            # ADD TO VOWELS
            add_item_to_dic(word[l], vowels)
 
        elif word[l] in consonants_list:
            letter_type = 'consonant'

            #ADD TO CONSONANTS
            add_item_to_dic(word[l], cons)

        else:
            letter_type = 'other'

        # ADD TO LETTERS
        add_item_to_dic(word[l], letters)
        
        if l != 0:
            if letter_type == 'consonant' and prev_letter_type == 'consonant':
                cl = prev_letter + word[l]

                # ADD TO CONS CLUSTERS
                add_item_to_dic(cl, cons_clusters)
            
            if letter_type == 'vowel' and prev_letter_type == 'vowel':
                cl = prev_letter + word[l]
                
                # ADD TO VOWEL CLUSTERS
                add_item_to_dic(cl, vowel_clusters)

        prev_letter = word[l]
        prev_letter_type = letter_type

#-------------------------------------#
# CONVERSION OF TOTALS TO FREQUENCIES #
#-------------------------------------#
convert_to_percent(total_letters, letters)
convert_to_percent(total_cons, cons)
convert_to_percent(total_vowels, vowels)
convert_to_percent(total_cons_cl, cons_clusters)
convert_to_percent(total_vowels_cl, vowel_clusters)


print("Letters: ", dict(sorted(letters.items(), key=lambda item: item[1], reverse=True)))
print()
print("Consonants: ", dict(sorted(cons.items(), key=lambda item: item[1], reverse=True)))
print()
print("Vowels: ", dict(sorted(vowels.items(), key=lambda item: item[1], reverse=True)))
print()
print("Cons Clusters: ", dict(sorted(cons_clusters.items(), key=lambda item: item[1], reverse=True)))
print()
print("Vowel Clusters: ", dict(sorted(vowel_clusters.items(), key=lambda item: item[1], reverse=True)))
