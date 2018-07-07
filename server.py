from src import app
from flask import render_template
from flask import jsonify,request

import sqlite3 as sql

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sql.connect('database.db')

con.row_factory = dict_factory

cur = con.cursor()



cur.execute("""CREATE TABLE IF NOT EXISTS  classment(

  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  score INT NOT NULL

  )""")



def insert(name,score):
    cur.execute("SELECT * FROM classment where lower(name)='"+name.lower()+"'")
    row=cur.fetchall()
    if (len(row)==0):
        cur.execute("INSERT INTO classment (name,score) VALUES (?,?)",(name,score))
        con.commit()
        return True
    else:
        cur.execute("UPDATE classment SET score='"+str(score)+"'Where name='"+name+"' and score>"+str(score))
        return False





@app.route('/')
def hello_world():
    cur.execute("SELECT * from classment")
    data =cur.fetchall()

    return jsonify(list(data))

@app.route('/add' , methods=['POST','GET'])
def add():
    if request.method=='POST':
        values = request.get_json()
        name=values.get('name')
        score=values.get('score')

        if insert(name,score):
            response = {
                'message': 'added succesfully',
                'score': score,
                'name': name
            }
            return jsonify(response), 200
        else :
            response = {
                'message': 'name exists but score overwritten',
                'score': score,
                'name': name
            }
            return jsonify(response),200
    elif request.method=='GET':
        response={
            'message':'Method not allowed'
        }
        return jsonify(response), 405


# Uncomment to add a new URL at /new

# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
