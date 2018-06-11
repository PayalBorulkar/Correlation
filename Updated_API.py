# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:46:45 2018

@author: Payal
"""

from flask import Flask, request, render_template
import sqlite3
from flask_restful import Resource, Api

app = Flask(__name__)

# Taking User_Handle number as input
@app.route('/')
def my_form():
    return render_template('Input.html')
#Displaying Summary of similar users
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    con = sqlite3.connect("My_Database.db")
    cur = con.cursor()
    cur.execute("Select * from corr_user2 WHERE User=? AND PearsonR=1 ORDER BY PearsonR DESC",(text,)) 
    rows = cur.fetchall()
    return render_template('Summary.html',rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
