import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('movie.db')

# Create the curser
c = conn.cursor()

c.execute("DROP TABLE movies")
# Create a "movies" table in "movie" database.
# DATATYES: NULL, INTEGER, REAL, TEXT, BLOB.
c.execute("""CREATE TABLE movies (
    name text,
    actor text,
    actress text,
    director text,
    year_of_release text    
    )""")
print("Created 'movies' table.\n")


# Insert in "movies" table in "movie" database.
movies_detail = [
                    ('Anbe Sivam', 'Kamal Hassan', 'Kiran', 'Sundar C', '2003'), 
                    ('Kannathil Muthamittal', 'R Madhavan', ' Simran', 'Manirathnam', '2002'), 
                    ('Kandukondain Kandukondain', 'Ajith', 'Tabu', 'Rajiv Menon', '2000'), 
                    ('M Kumaran Son Of Mahalakshmi', 'Jayam Ravi', 'Asin', 'M Raja', '2004'), 
                    ('Mozhi', 'Prithviraj Sukumaran', 'Jyothika', 'Radha Mohan', '2007'),
                    ('Manmadhan Ambu', ' Kamal Hassan', 'Trisha', 'K S Ravikumar', '2010'),
                    ('Vikram2', 'Kamal Hassan', '', 'Lokesh Kanakaraj', '2022')
                ]
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movies_detail)
print("Inserted values into 'movies' table successfully.\n")

# Query the database;
# QUERY 1: Select all movie detail with row id.
print("Query 1: Select all movie detail.")
c.execute("SELECT * FROM movies") # Will create the query.
# To actually fetch the details use: c.fetchone(), c.fetchmany(3), c.fetchall()
all_movies_detail = c.fetchall()
for movie in all_movies_detail:
    print(movie)
print()
# QUERY 2: Select all movie detail with row id.
print("Query 2: Select all movie detail with row id.")
c.execute("SELECT rowid,* FROM movies") # Will create the query.
# To actually fetch the details use: c.fetchone(), c.fetchmany(3), c.fetchall()
query2 = c.fetchall()
for movie in query2:
    print(movie)
print()
# QUERY 3: Select movie deail in which 'Kamal Hassan' is the actor.
print("Query 3: Select movie names in which ;Kamal Hassan' is the actor.")
c.execute("SELECT name FROM movies WHERE actor='Kamal Hassan'")
query3 = c.fetchall()
for movie in query3:
    print(movie)
print()
# QUERY 4: Select movie names in which 'Kamal Hassan' is the actor.
print("Query 4: Select movie names in which ;Kamal Hassan' is the actor.")
c.execute("SELECT name FROM movies WHERE actor='Kamal Hassan'")
query4 = c.fetchall()
for name in query4:
    print(name)
print()


# Commit our command
conn.commit()

# Close our connection
conn.close()