import sqlite3

# step 1: connect to the database or create it if it doesn't exist
connection = sqlite3.connect('my_database.db')

# step 2: create a cursor object to interact with the database
cursor = connection.cursor()

# step 3: create a table (if it doesn't already exist)
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
)""")

# step 4: insert some data into the table
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 22, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Charlie', 19, 'A')")

# step 5: commit the changes to the database
connection.commit()

# step 6: query the data from the table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)