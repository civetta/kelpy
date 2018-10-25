from flask import Flask, render_template, redirect, url_for,abort
from random import randint
import sqlite3
import pandas as pd
import math
app = Flask(__name__)
 

def connect_to_database():
    con = sqlite3.connect("blog_posts.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return cur

@app.route("/page_<var_page_num>")
def split_posts(var_page_num):
    cur = connect_to_database()
    cur.execute("select * from blog_data")
    db_rows = cur.fetchall()
    total_pages = math.ceil(len(db_rows)/float(3))
    start_post = (int(var_page_num)*3)-3
    db_rows = db_rows[start_post:start_post+3]
    return render_template("index.html",rows = db_rows, current_page = int(var_page_num),max_page=total_pages)

@app.route("/")
def index():
    return redirect(url_for('split_posts', var_page_num=1))

@app.route("/posts/<var_post_title>")
def blog_post(var_post_title):
    cur = connect_to_database()
    cur.execute("select * from blog_data Where post_title = ?",(var_post_title,))
    row = cur.fetchone()
    if row != None:
        return render_template("individual_blog_post.html", content = row)
    else:
        return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
