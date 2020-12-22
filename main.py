from package.database.database import LORConnect

def run():
    db = LORConnect()
    db.get_parts()

if __name__ == "__main__":
    run()