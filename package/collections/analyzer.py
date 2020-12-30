import organizer as org

words_list = org.get_words()
vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
consonants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

letters, cons, vowels = {}, {}, {}
start_letters, start_cons, start_vowels = {}, {}, {}
mid_letters, mid_cons, mid_vowels = {}, {}, {}
end_letters, end_cons, end_vowels = {}, {}, {}
letter_clusters, cons_clusters, vowel_clusters = {}, {}, {}
start_cons_clusters, mid_cons_clusters, end_cons_clusters = {}, {}, {}
start_vow_clusters, mid_vow_clusters, end_vow_clusters = {}, {}, {}

letter_type, prev_letter, prev_letter_type, letter_type_list = '', '', '', ''

tot_letters, tot_cons, tot_vowels = 0, 0, 0
tot_start_letters, tot_start_cons, tot_start_vowels = 0, 0, 0
tot_mid_letters, tot_mid_cons, tot_mid_vowels = 0, 0, 0
tot_end_letters, tot_end_cons, tot_end_vowels = 0, 0, 0
tot_letter_cl, tot_cons_cl, tot_vowels_cl = 0, 0, 0
tot_start_cons_cl, tot_mid_cons_cl, tot_end_cons_cl = 0, 0, 0
tot_start_vow_cl, tot_mid_vow_cl, tot_end_vow_cl = 0, 0, 0


# Adds item to the specified dictionary
def add_item_to_dic(item, dic):
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

def dispatch_cluster(letter_type_list, letter_type, prev_letter_type, is_beginning=False, is_end=False):
    if len(letter_type_list) > 1:
        cl = letter_type_list
        add_item_to_dic(cl, letter_clusters)
        if prev_letter_type == 'consonant':
            add_item_to_dic(cl, cons_clusters)
            if is_end:
                add_item_to_dic(cl, end_cons_clusters)
            elif is_beginning:
                add_item_to_dic(cl, start_cons_clusters)
            else:
                add_item_to_dic(cl, mid_cons_clusters)
        else:
            add_item_to_dic(cl, vowel_clusters)     
            if is_end:
                add_item_to_dic(cl, end_vow_clusters)
            elif is_beginning:
                add_item_to_dic(cl, start_vow_clusters)
            else:
                add_item_to_dic(cl, mid_vow_clusters)     
    if letter_type != 'other':
        letter_type_list = word[l]
    else:
        letter_type_list = ''

    return letter_type_list

for word in words_list:
    is_beginning = True
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
                    letter_type_list = dispatch_cluster(letter_type_list, letter_type, prev_letter_type, is_end=True)
                    
                    add_item_to_dic(word[l], end_letters)
                    if letter_type == 'consonant':
                        add_item_to_dic(word[l], end_cons)
                    elif letter_type == 'vowel':
                        add_item_to_dic(word[l], end_vowels)
                else:
                    
                    add_item_to_dic(word[l], mid_letters)
                    if letter_type == 'consonant':
                        add_item_to_dic(word[l], mid_cons)
                    elif letter_type == 'vowel':
                        add_item_to_dic(word[l], mid_vowels)
            else:
                letter_type_list = dispatch_cluster(letter_type_list, letter_type, prev_letter_type, is_beginning)
                is_beginning = False
        else:
            letter_type_list = word[l]
            is_beginning = True
            
            add_item_to_dic(word[l], start_letters)
            if letter_type == 'consonant':
                add_item_to_dic(word[l], start_cons)
            elif letter_type == 'vowel':
                add_item_to_dic(word[l], start_vowels)
        
        prev_letter = word[l]
        prev_letter_type = letter_type


# FILTERING LOW VALUES
def remove_lower_values(dic, val):
    for k, v in dict(dic).items():
        if v < val:
            del dic[k]

remove_lower_values(cons_clusters, 1)
remove_lower_values(vowel_clusters, 1)


# CONVERSION OF TOTALS TO FREQUENCIES
def convert_to_percent(total, dic):
    for d in dic:
        total += dic[d]
    for d in dic:
        dic[d] = round(dic[d]/total*100, 5)

convert_to_percent(tot_letters, letters)
convert_to_percent(tot_cons, cons)
convert_to_percent(tot_vowels, vowels)

convert_to_percent(tot_start_letters, start_letters)
convert_to_percent(tot_start_cons, start_cons)
convert_to_percent(tot_start_vowels, start_vowels)
convert_to_percent(tot_mid_letters, mid_letters)
convert_to_percent(tot_mid_cons, mid_cons)
convert_to_percent(tot_mid_vowels, mid_vowels)
convert_to_percent(tot_end_letters, end_letters)
convert_to_percent(tot_end_cons, end_cons)
convert_to_percent(tot_end_vowels, end_vowels)

convert_to_percent(tot_letter_cl, letter_clusters)
convert_to_percent(tot_cons_cl, cons_clusters)
convert_to_percent(tot_vowels_cl, vowel_clusters)

convert_to_percent(tot_start_cons_cl, start_cons_clusters)
convert_to_percent(tot_mid_cons_cl, mid_cons_clusters)
convert_to_percent(tot_end_cons_cl, end_cons_clusters)
convert_to_percent(tot_start_vow_cl, start_vow_clusters)
convert_to_percent(tot_mid_vow_cl, mid_vow_clusters)
convert_to_percent(tot_end_vow_cl, end_vow_clusters)


# PRINTING THE OUTPUT
def print_result(title, dic):
    ruler = ''
    for r in range(len(title)):
        ruler += '='

    print()
    print(title)
    print(ruler)
    print(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))

# print_result('Letters', letters)
# print_result('Consonants', cons)
# print_result('Vowels', vowels)
# print_result('Start Letters', start_letters)
# print_result('Start Cons', start_cons)
# print_result('Start Vowels', start_vowels)
# print_result('Mid Letters', mid_letters)
# print_result('Mid Cons', mid_cons)
# print_result('Mid Vowels', mid_vowels)
# print_result('End Letters', end_letters)
# print_result('End Cons', end_cons)
# print_result('End Vowels', end_vowels)
# print_result('Letter Clusters', letter_clusters)
# print_result('Consonant Clusters', cons_clusters)
# print_result('Vowel Clusters', vowel_clusters)
# print_result('Start Cons Clusters', start_cons_clusters)
# print_result('Mid Cons Clusters', mid_cons_clusters)
# print_result('End Cons Clusters', end_cons_clusters)
# print_result('Start Vow Clusters', start_vow_clusters)
# print_result('Mid Vow Clusters', mid_vow_clusters)
# print_result('End Vow Clusters', end_vow_clusters)

def dic_pack(dic, property):
    package = []
    for key, value, in dic.items():
        item = { key: { 'property': property, 'frequency': value }}
        package.append(item)
    return package

letters = dic_pack(letters, 'any')

print(letters)
# print(analysis)