import sqlite3

conn = sqlite3.connect("data.sqlite")

cursor = conn.cursor()
# team_query = """ CREATE TABLE team (
#     id integer PRIMARY KEY,
#     name text NOT NULL,
#     alive boolean NOT NULL,
#     status text NOT NULL,
#     sick text NOT NULL
# )"""
# cursor.execute(team_query)

user_query = """ CREATE TABLE user (
    username text PRIMARY KEY,
    highscore integer NOT NULL
)"""
cursor.execute(user_query)

# game_data_query = """ CREATE TABLE game (
#     id integer PRIMARY KEY,
#     money integer NOT NULL,
#     food integer NOT NULL,
#     camels integer NOT NULL,
#     clothes integer NOT NULL,
#     bullets integer NOT NULL,
#     hunger integer NOT NULL,
#     exhaustion integer NOT NULL,
#     total_distance integer NOT NULL,
#     days integer NOT NULL
# )"""
# cursor.execute(game_data_query)