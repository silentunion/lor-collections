from package.insertions import insert_parts
from package.database import database

def run():
    ins = insert_parts.Insertions()
    ins.add_frequencies()

if __name__ == "__main__":
    run()