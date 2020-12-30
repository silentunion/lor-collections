import organizer as org

words_list = org.get_words()
vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

letters, cons, vowels = {}, {}, {}
cons_clusters, vowel_clusters = {}, {}

letter_type = ''
prev_letter = ''
prev_letter_type = ''
letter_type_list = ''

total_letters, total_cons, total_vowels = 0, 0, 0
total_cons_cl, total_vowels_cl = 0, 0

# Adds item to the specified dictionary
def add_item_to_dic(item, dic):
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

def dispatch_cluster(letter_type_list, letter_type, prev_letter_type):
    if len(letter_type_list) > 1:
        cl = letter_type_list
        if prev_letter_type == 'consonant':
            add_item_to_dic(cl, cons_clusters)
        else:
            add_item_to_dic(cl, vowel_clusters)          
    if letter_type != 'other':
        letter_type_list = word[l]
    else:
        letter_type_list = ''

    return letter_type_list

for word in words_list:
    for l in range(len(word)):
        if word[l] in vowels_list:
            letter_type = 'vowel'
            add_item_to_dic(word[l], vowels)
 
        elif word[l] in consonants_list:
            letter_type = 'consonant'
            add_item_to_dic(word[l], cons)

        else:
            letter_type = 'other'

        if letter_type != 'other':
            add_item_to_dic(word[l], letters)
        
        if l != 0:
            if letter_type == prev_letter_type and letter_type != 'other':
                letter_type_list += word[l]
                if l == len(word)-1:
                    letter_type_list = dispatch_cluster(letter_type_list, letter_type, prev_letter_type)
            else:
                letter_type_list = dispatch_cluster(letter_type_list, letter_type, prev_letter_type)
        else:
            letter_type_list = word[l]
        
        prev_letter = word[l]
        prev_letter_type = letter_type


# FILTERING LOW VALUES
def remove_lower_values(dic, val):
    for k, v in dict(dic).items():
        if v < val:
            del dic[k]

remove_lower_values(cons_clusters, 2)
remove_lower_values(vowel_clusters, 2)


# CONVERSION OF TOTALS TO FREQUENCIES
def convert_to_percent(total, dic):
    for d in dic:
        total += dic[d]
    for d in dic:
        dic[d] = round(dic[d]/total*100, 5)

convert_to_percent(total_letters, letters)
convert_to_percent(total_cons, cons)
convert_to_percent(total_vowels, vowels)
convert_to_percent(total_cons_cl, cons_clusters)
convert_to_percent(total_vowels_cl, vowel_clusters)


# PRINTING THE OUTPUT
def print_result(title, dic):
    ruler = ''
    for r in range(len(title)):
        ruler += '='

    print()
    print(title)
    print(ruler)
    print(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))

print_result('Letters', letters)
print_result('Consonants', cons)
print_result('Vowels', vowels)
print_result('Consonant Clusters', cons_clusters)
print_result('Vowel Clusters', vowel_clusters)
