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
                print('Added letter ' + parts[p] + ' to collection ' + collection + ' with prop ' + properties[p])

        else:
            print('List lengths do not match')
    
    def insert_clusters(self):
        v, c = 'vowel', 'consonant'

        parts = ['ae', 'ai', 'ao', 'au', 'ay',
            'ea', 'ee', 'ei', 'eo', 'eu', 'ey',
            'ia', 'ie', 'io', 'iu',
            'oa', 'oe', 'oi', 'oo', 'ou', 'oy',
            'ua', 'ue', 'ui', 'uo', 'uy',
            'ya', 'ye', 'yi', 'yo', 'yu']
        category = 'clusters'
        collection = 'English Basic'
        properties = v

        for p in range(0, len(parts)):
            db.insert_part(parts[p], category)
            db.add_part_to_collection(parts[p], category, collection)
            db.add_prop_to_part(parts[p], category, collection, properties)
            print('Added letter ' + parts[p] + ' to collection ' + collection + ' with prop ' + properties)


    def add_frequencies(self):
        parts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        category = 'letters'
        collection = 'English Basic'
        freqs = ["0.084966", "0.020720", "0.045388", "0.033844", "0.111607",
        "0.018121", "0.024705", "0.030034", "0.075448", "0.001965", "0.011016",
        "0.054893", "0.030129", "0.066544", "0.071635", "0.031671", "0.001962",
        "0.075809", "0.057351", "0.069509", "0.036308", "0.010074", "0.012899",
        "0.002902", "0.017779", "0.002722"]

        if len(parts) == len(freqs):
            for p in range(0, len(parts)):
                db.add_freq_to_part(parts[p], category, collection, freqs[p])
                print('Applied freq ' + freqs[p] + ' to letter ' + parts[p])

        else:
            print('List lengths do not match')


        print(len(parts), len(freqs))