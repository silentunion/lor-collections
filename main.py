from package.database.database import LORConnect

def run():
    db = LORConnect()
    print(db.get_col_part_if_exists('i', 'letters', 'English Basic'))
    db.get_parts()

if __name__ == "__main__":
    run()