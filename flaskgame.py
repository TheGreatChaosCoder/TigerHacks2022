from flaskmain import dbConnection
from flask import Flask, redirect, url_for, render_template, request
import sqlite3

def resetObjects() -> None:
    try:
        msg = ""
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute("TRUNCATE TABLE game")
            cur.execute("INSERT INTO game (money, food, camels, clothes, bullets, hunger, exhaustion, total_distance, days) VALUES (?,?,?,?,?,?,?,?,?)",
                (1600, 60000, 4, 4, 0, 3, 0, 0, 0) )
            con.commit()
            msg = "Reset successful"
            return
    except:
         con.rollback()
         msg = "error in insert operation"
         return 
    finally:
        return
        con.close()

def getGameData(data : str):
    try:
        msg = ""
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute(f"SELECT * FROM game")
            
            con.commit()
            msg = "Got data sucessfully"
    except:
         con.rollback()
         msg = "failed to read data"
      
    finally:
        rows = cur.fetchall()
        return rows
        con.close()


