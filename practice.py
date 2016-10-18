from flask import Flask, jsonify, session, redirect
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from flaskext.mysql import MySQL
import bcrypt
import jwt

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'x'
app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
app.config['MYSQL_DATABASE_DB'] = 'devcamp'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['CORS_HEADERS'] = 'Content-Type'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'


cursor.execute("SELECT COUNT(id) FROM category")
counter = cursor.fetchone()
display = []
for i in range(1, counter[0] + 1):
    cursor.execute(
        "SELECT category.id AS CAT_Id, category.title AS CAt_Title, forums.id, forums.title, forums.last_post, forums.description, forums.permissions FROM forums LEFT JOIN category ON forums.cat_id = category.id WHERE cat_id = %s",
        i)
    result = cursor.fetchall()
    forum_array = []
    for j in range(len(result)):
        forum_array.append(
            {"id": result[j][2], "title": result[j][3], "last_post": result[j][4], "description": result[j][5],
             "permissions": result[j][6]})
    display.append({"id": result[0][0], "title": result[0][1], "forums": forum_array})


if __name__ == '__main__':
    app.run(debug=True)
