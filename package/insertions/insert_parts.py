from ..database.database import LORConnect

db = LORConnect()

class Insertions():
    def insert_alphabet(self):
        v, c = 'vowel', 'consonant'

        parts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        category = 'letters'
        collection = 'English Basic'
        properties = [v, c, c, c, v, c, c, c, v, c, c, c, c, c, v, c, c, c, c, c, v, c, c, c, v, c]

        if len(parts) == len(properties):
            for p in range(0, len(parts)):
                db.insert_part(parts[p], category)
                db.add_part_to_collection(parts[p], category, collection)
                db.add_prop_to_part(parts[p], category, collection, properties[p])

        else:
            print('List lengths do not match')
    