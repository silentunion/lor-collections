from ..database.database import LORConnect

db = LORConnect()

v, c = 'vowel', 'consonant'

parts = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
category = 'letters'
collection = 'English Basic'
properties = [v, c, c, c, c, c, v, c, c, c, c, c, v, c, c, c, v, c]

if len(parts) == len(properties):
    for p in range(0, len(parts)):
        db.insert_part(parts[p], category)
        db.add_part_to_collection(parts[p], category, collection)
        db.add_prop_to_part(parts[p], category, collection, properties[p])
    
        print('Added part ' + parts[p] + ' category ' + category + ' prop ' + properties[p])

else:
    print('List lengths do not match')