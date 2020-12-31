from package.insertions import insert_parts
from package.database import database

def run():
    ins = insert_parts.Insertions()

    # ins.insert_alphabet()

    ins.insert_analysis()

    # print("Inserting clusters")
    # ins.insert_clusters()
    # print("Inserting frequencies")
    # ins.add_frequencies()
    # print("Insertions complete")

if __name__ == "__main__":
    run()