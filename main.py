from package.database.database import LORConnect

def run():
    db = LORConnect()
    print(db.get_part_id_if_exists('a', 'letters'))
    print(db.get_col_id_if_exists('English'))
    db.get_parts()

if __name__ == "__main__":
    run()