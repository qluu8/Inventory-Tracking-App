import sqlite3

db_name = "inventory.db"

def get_connection():
    return sqlite3.connect(db_name)

def create_tables():
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cardN TEXT NOT NULL,
            cardID TEXT NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            location TEXT NOT NULL
        )
                   """)
    
    connect.commit()
    connect.close()