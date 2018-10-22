from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import sqlite3
import pandas as pd
app = Flask(__name__)
 
con = sqlite3.connect("kelpy_db.db")
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("select * from blog_post")
rows = cur.fetchall()
df = pd.DataFrame(rows)
print df

@app.route("/")
def index():
    return render_template("index.html",rows = rows)
 
if __name__ == "__main__":
    app.run()
