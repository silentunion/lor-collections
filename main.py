from package.database.database import LORConnect

def run():
    db = LORConnect()
    db.add_prop_to_part('h', 'letters', 'English Basic', 'is_consonant')
    db.get_parts()

if __name__ == "__main__":
    run()