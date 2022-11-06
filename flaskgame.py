from flaskmain import dbConnection
from flask import Flask, redirect, url_for, render_template, request
import sqlite3

def resetObjects() -> None:
    try:
        msg = "" 
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute("DELETE from game")
            con.commit()
            cur.execute("INSERT INTO game (id, money, food, camels, clothes, bullets, hunger, exhaustion, total_distance, days) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (0, 1600, 0, 4, 4, 0, 3, 0, 0, 1) )
            con.commit()
            msg = "Reset successful"
    except:
         con.rollback()
         msg = "error in insert operation"
    finally:
        return
        con.close()

def getGameData(data : str):
    try:
        msg = ""
        with dbConnection() as con:
            cur = con.cursor()
            cur.execute(f"SELECT {data} FROM game ORDER BY id ASC LIMIT 1")
            
            con.commit()
            msg = "Got data sucessfully"
    except:
         con.rollback()
         msg = "failed to read data"
      
    finally:
        rows = cur.fetchall()
        return rows[0][0]
        con.close()
