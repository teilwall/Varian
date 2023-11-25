import sqlite3

def drop_all_tables(database_path):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Disable foreign key constraints temporarily
    cursor.execute('PRAGMA foreign_keys=off;')
    connection.commit()

    # Get a list of all tables and drop them (excluding sqlite_sequence)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        cursor.execute(f'DROP TABLE IF EXISTS {table_name};')

    # Reset foreign key constraints
    cursor.execute('PRAGMA foreign_keys=on;')
    connection.commit()

    # Close the connection
    connection.close()

if __name__ == "__main__":
    database_path = "LifeExtensionApp/db.sqlite3"
    drop_all_tables(database_path)
