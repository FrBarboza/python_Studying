import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

create_db = 'CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, diaria real, cidade text)'

load_hotel = "INSERT INTO 'hoteis' (hotel_id, nome, estrelas, diaria, cidade)\
    VALUES ('alpha','Hotel Alpha', 4.4, 345.77,'Santo André')";

cursor.execute(create_db)
cursor.execute(load_hotel)

connection.commit()
connection.close()
