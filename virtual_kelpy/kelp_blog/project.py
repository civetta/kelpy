from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import sqlite3
import pandas as pd
app = Flask(__name__)
 

def connect_to_database():
    con = sqlite3.connect("kelpy_db.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return cur

@app.route("/")
def index():
    cur = connect_to_database()
    cur.execute("select * from blog_post")
    db_rows = cur.fetchall()
    return render_template("index.html",rows = db_rows)

@app.route("/posts/<var_post_title>")
def blog_post(var_post_title):
    cur = connect_to_database()
    var_post_title=str(var_post_title)
    cur.execute("select * from blog_post Where post_title = ?",(var_post_title,))
    row = cur.fetchone()
    return render_template("individual_blog_post.html", content = row)



if __name__ == "__main__":
    app.run(debug=True)
