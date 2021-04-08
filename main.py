from package.insertions import insert_parts
from package.database import database
from package.collections import organizer

import os

def run():
    # ins = insert_parts.Insertions()

    # ins.insert_alphabet()

    # ins.insert_analysis()

    # print("Inserting clusters")
    # ins.insert_clusters()
    # print("Inserting frequencies")
    # ins.add_frequencies()
    # print("Insertions complete")
    org = organizer.Collections()

    path = '\\resources\\2020-2 UNLOCODE CodeList.txt'

    org.get_words_from_txt(path, 'JP')

if __name__ == "__main__":
    run()