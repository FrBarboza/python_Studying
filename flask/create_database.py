import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_db = 'CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, diaria real, cidade text)'

load_hotel = "INSERT INTO hoteis VALUES ('hoteis_id', 'alpha', 4.3, 432.99,'Sao Paulo')"

cursor.execute(create_db)
cursor.execute(load_hotel)

connection.commit()
connection.close()
