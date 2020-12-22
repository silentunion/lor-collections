from package.database.database import LORConnect

def run():
    db = LORConnect()
    # db.add_part_to_collection('h', 'letters', 'English Basic')
    db.get_parts()

if __name__ == "__main__":
    run()