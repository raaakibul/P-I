import sqlite3

connection = sqlite3.connect("mydata.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons(
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)

""")

cursor.execute("""
INSERT INTO persons VALUES
('Paul', 'Smith', 24).
('Ana', 'Isabela',25),
('John', 'Ball', 28)

""")


connection.commit()

connection.close()