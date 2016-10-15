from flask import Flask, jsonify, session, redirect
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from flaskext.mysql import MySQL 
import bcrypt 
from flask_cors import CORS 
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

cors = CORS(app)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


@app.route('/api/hello', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def hello_world():
    return jsonify({
        "hello": "Hello, world!"
    })


@app.route('/api/login', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def login():
    user_name = request.get_json()['username'].encode('utf-8')
    req_pass = request.get_json()['password'].encode('utf-8')
    check_username = "SELECT password FROM users WHERE username = %s"
    cursor.execute(check_username, user_name)
    result = cursor.fetchone()
    if result is None:
        return jsonify(status=401, message="Please check your user name as we can't find it in our system")
    elif bcrypt.checkpw(req_pass, result[0].encode('utf-8')):
        check_id = "SELECT id FROM users WHERE username = %s"
        cursor.execute(check_id, user_name)
        user_id = cursor.fetchone()
        session['id'] = jwt.encode({'id': user_id[0]}, 'H4mb0l0gn4', algorithm='HS256')
        session['username'] = user_name
        return jsonify(status = 200, token = session['id'])
    else:
        return jsonify(status=401, message="Incorrect Password.  Please try again.")

@app.route('/api/register', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*') 
def register():
    # Check to See if the Username is already taken
    check_username = "SELECT * FROM user WHERE user_name = %s"
    cursor.execute(check_username, request.get_json()['userName'])
    result=cursor.fetchone()
    if result is None:
        full_name = request.get_json()['fullName']
        password = request.get_json()['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        user_name = request.get_json()['userName']
        email = request.get_json()['email']
        avatar = request.get_json()['avatar']
        session['username'] = user_name
        title = request.get_json()['title'] 
        cursor.execute("INSERT INTO user VALUES (DEFAULT, %s, %s, DEFAULT, %s, %s, %s, %s, %s)", (full_name, title, user_name, hashed_password, avatar, email, rank_id))
        conn.commit()
        cursor.execute('SELECT id FROM users WHERE user_name = %s')
        id_return = cursor.fetchone()
        session['id'] = jwt.encode({'id': id_return[0]}, 'H4mb0l0gn4', algorithm='HS256')
        return jsonify(status=200, token=session['id'])
    else:
        return jsonify(status=401, message="User Name Already In Use Please Choose Another")

@app.route('/api/main', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*') 
def main():
    blog_feed = "SELECT author, author_id, date, article FROM blog LEFT JOIN users on blog.author = users.username ORDER BY date DESC"
    cursor.execute(blog_feed)
    result = cursor.fetchall()
    if result == ():
        return jsonify(status=401, message="We seem to be having trouble with our servers.  Please refresh the page.")
    else:
        return jsonify(status=200, blogs=result)

@app.route('/api/follow/<id>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*') 
def user_portal(id):
    cursor.execute("INSERT INTO connections VALUES (DEFAULT, %s, %s)", (session['username'], id))
    conn.commit()

@app.route('/api/user_portal', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def user_portal():
    cursor.execute("SELECT author, author_id, date, article, category.title, description FROM blog LEFT JOIN users ON blog.author = users.username LEFT JOIN category on blog.category_id = category.id LEFT JOIN connections ON users.id = connections.followed WHERE connections.follower = %s ORDER BY date DESC", session['username'])
    blog_feed = cursor.fetchall()
    cursor.execute("SELECT full_name, title, username, avatar, email, rank_id FROM users WHERE username = session['username']")
    user_data = cursor.fetchall()
    return jsonify(status=200, blog_feed=blog_feed, user_data)

@app.route('/api/blog_post', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def user_portal():
    article = request.get_json()['blog_post']
    cursor.execute("SELECT id from users WHERE username = %s", session['username'])
    author_id = fetchone()
    cursor.execute("INSERT INTO blog VALUES (DEFAULT, %s, DEFAULT, %s, %s, %s)", (session['username'], article, author_id, category_id))
    conn.commit()


if __name__ == '__main__':
    app.run(debug=True)
