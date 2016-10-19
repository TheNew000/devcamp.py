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

app.config['MYSQL_DATABASE_USER'] = 'root'
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
        return jsonify(status=200, token=session['id'])
    else:
        return jsonify(status=401, message="Incorrect Password.  Please try again.")


@app.route('/api/register', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def register():
    # Check to See if the Username is already taken
    check_username = "SELECT * FROM user WHERE user_name = %s"
    cursor.execute(check_username, request.get_json()['userName'])
    result = cursor.fetchone()
    if result is None:
        full_name = request.get_json()['fullName']
        password = request.get_json()['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        user_name = request.get_json()['userName']
        email = request.get_json()['email']
        avatar = request.get_json()['avatar']
        session['username'] = user_name
        title = request.get_json()['title']
        cursor.execute("INSERT INTO user VALUES (DEFAULT, %s, %s, DEFAULT, %s, %s, %s, %s, %s)",
                       (full_name, title, user_name, hashed_password, avatar, email, 3))
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
    blog_feed = "SELECT author, author_id, date, article FROM blog LEFT JOIN users ON blog.author = users.username ORDER BY date DESC"
    cursor.execute(blog_feed)
    result = cursor.fetchall()
    if result == ():
        return jsonify(status=401, message="We seem to be having trouble with our servers.  Please refresh the page.")
    else:
        return jsonify(status=200, blogs=result)


@app.route('/api/follow/<id>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def follow(id):
    cursor.execute("INSERT INTO connections VALUES (DEFAULT, %s, %s)", (session['username'], id))
    conn.commit()


@app.route('/api/user_portal', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def user_portal():
    cursor.execute(
        "SELECT author, author_id, date, article, category.title, description FROM blog LEFT JOIN users ON blog.author = users.username LEFT JOIN category ON blog.category_id = category.id LEFT JOIN connections ON users.id = connections.followed WHERE connections.follower = %s ORDER BY date DESC",
        session['username'])
    blog_feed = cursor.fetchall()
    cursor.execute(
        "SELECT full_name, title, username, avatar, email, rank_id FROM users WHERE username = session['username']")
    user_data = cursor.fetchall()
    return jsonify(status=200, blog_feed=blog_feed, user_data=user_data)


#######################################
#######################################
#######################################
# FUNCTIONALITY FOR BLOGS:

@app.route('/api/blogs', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def blogs():
    cursor.execute(
        "SELECT author, author_id, date, article, count(followed) AS fcount FROM blog LEFT JOIN users ON blog.author = users.username LEFT JOIN connections ON users.id = connections.followed GROUP BY author_id, author, date, article ORDER BY fcount DESC")
    popular_blogs = cursor.fetchall()
    cursor.execute("SELECT author, author_id, date, article FROM blog ORDER BY date DESC")
    blog_feed = cursor.fetchall()
    return jsonify(status=200, popular_blogs=popular_blogs, blog_feed=blog_feed)


@app.route('/api/blog_search/<category>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def blog_search(category):
    if category == 'FAVE':
        cursor.execute(
            "SELECT author, author_id, date, article FROM blog LEFT JOIN favorites ON blog.id = category.blog_id WHERE fave = '1' AND username = %s ORDER BY date DESC",
            session['username'])
    elif category == 'Custom_Search':
        user_query = request.get_json()['user_search']
        cursor.execute(
            "SELECT ID, Author, Title, Description, Article, Date_Posted, Occurance, Fave_Count, (Occurance + Fave_Count) AS Total FROM (SELECT T1.id AS ID, T1.author AS Author, T1.date AS Date_Posted, T1.title AS Title, T1.description AS Description, T1.article AS Article, T1.occurance AS Occurance, COUNT(CASE WHEN fave='1' THEN `fave` END) AS Fave_Count FROM (SELECT id, author, date, article, (length(article) - length(replace(article,'%r',''))) / length('%r') AS occurance FROM blog ORDER BY occurance DESC) AS T1 LEFT JOIN favorites ON T1.id = favorites.blog_id WHERE T1.occurance > 0 GROUP BY ID, Occurance) AS T2 ORDER BY Total DESC",
            (user_query, user_query))
    else:
        cursor.execute(
            "SELECT author, author_id, date, article FROM blog LEFT JOIN category ON blog.id = favorites.blog_id WHERE %s = 'TRUE' ORDER BY DATE DESC",
            category)
    blog_feed = cursor.fetchall()
    if blog_feed is None:
        return jsonify(status=401, message="Sorry but no results match your query!")
    else:
        return jsonify(status=200, blog_feed=blog_feed)


@app.route('/api/blog_post', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def blog_post():
    article = request.get_json()['blog_post']
    cursor.execute("SELECT id FROM users WHERE username = %s", session['username'])
    author_id = cursor.fetchone()
    if author_id is None:
        return jsonify(status=401, message="Please Log In to Interact")
    else:
        cursor.execute("INSERT INTO blog VALUES (DEFAULT, %s, DEFAULT, %s, %s)",
                       (session['username'], article, author_id))
        conn.commit()
        return jsonify(status=200, message="Blog Post Successfully Added!")


# END BLOG FUNCTIONALITY
#######################################
#######################################
#######################################

# FUNCTIONALITY FOR FORUMS:
@app.route('/api/forum_main', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def forum_main():
    cursor.execute("SELECT COUNT(id) FROM category")
    counter = cursor.fetchone()
    display = []
    for i in range(1, int(counter[0]) + 1):
        cursor.execute(
            "SELECT category.id AS CAT_Id, category.title AS Cat_Title, forums.id, forums.title, forums.last_post, forums.description, forums.permissions FROM forums LEFT JOIN category ON forums.cat_id = category.id WHERE cat_id = %s",
            i)
        result = cursor.fetchall()
        forum_array = []
        for j in range(len(result)):
            forum_array.append(
                {"id": result[j][2], "title": result[j][3], "last_post": result[j][4], "description": result[j][5],
                 "permissions": result[j][6]})
        display.append({"id": result[0][0], "title": result[0][1], "forums": forum_array})
    return jsonify(status=200, display=display)


@app.route('/api/get_forum/<id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def get_forum(id):
    cursor.execute(
        "SELECT forums.title, thread.*, users.username FROM thread LEFT JOIN forums ON forums.id = thread.forum_id LEFT JOIN users ON thread.author_id = users.id WHERE thread.forum_id = %s",
        id)
    result = cursor.fetchall()

    if result == ():
        return jsonify(status=401, message="No results match your query")
    else:
        cursor.execute("SELECT COUNT(thread_id) FROM thread_reply WHERE thread_id = %s", id)
        thread_count = cursor.fetchone()

        if thread_count is None:
            count = 0
        else:
            count = thread_count[0]

        thread_array = []

        for i in range(len(result)):
            thread_array.append(
                {"title": result[i][2], "id": result[i][1], "author": result[i][9], "reply_count": count,
                 "post_time": result[i][5]})

        thread_object = {'forum_title': result[0][0], 'forum_id': result[0][6], 'threads': thread_array}
        return jsonify(status=200, thread_object=thread_object)


@app.route('/api/get_thread/<id>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def get_thread(id):
    # cursor.execute("SELECT T2.*, users.username AS Rep_Auth_User FROM (SELECT T1.*, users.username AS T_Auth_Username FROM (SELECT thread.title, thread.id AS Thread_ID, thread.post_content as thread_content, thread.author_id AS Thread_Author, thread_reply.post_content, thread_reply.id AS Reply_ID, thread_reply.author_id AS Reply_Author, thread_reply.created AS Post_Time FROM thread LEFT JOIN thread_reply ON thread_reply.thread_id = thread.id WHERE thread.id = %s) AS T1 LEFT JOIN users ON users.id = T1.Thread_Author) AS T2 LEFT JOIN users ON users.id = T2.Reply_Author", id)
    # result = cursor.fetchall()
    cursor.execute(
        "SELECT thread.title, thread.id, thread.post_content, users.username AS Thread_Author FROM thread LEFT JOIN users ON users.id = thread.author_id WHERE thread.id = %s",
        id)
    thread_info = cursor.fetchone()

    thread_object = {
        "content": thread_info[2],
        "title": thread_info[0],
        "id": thread_info[1],
        "author": thread_info[3]
    }

    cursor.execute(
        "SELECT thread_reply.post_content, thread_reply.id, users.username AS Reply_Author, thread_reply.created FROM thread_reply LEFT JOIN users ON thread_reply.author_id = users.id WHERE thread_reply.thread_id = %s",
        id)
    reply_info = cursor.fetchall()
    if reply_info == ():
        return jsonify(status=200, thread_object=thread_object)
    else:
        reply_array = []
        for i in range(len(reply_info)):
            reply_array.append({"content": reply_info[i][0], "id": reply_info[i][1], "author": reply_info[i][2], "post_time": reply_info[i][3]})
            thread_object = {'title': thread_info[0], 'id': thread_info[1], 'content': thread_info[2], 'author': thread_info[3], 'replies': reply_array}
            return jsonify(status=200, thread_object=thread_object)


@app.route('/api/create_thread/<id>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def create_thread(id):
    cursor.execute("INSERT INTO thread VALUES (DEFAULT, %s, %s, %s, DEFAULT, %s, 0, 0)",
                   (request.get_json()['title'], request.get_json()['author_id'], request.get_json()['content'], id))

    conn.commit()

    return jsonify(status=200)


@app.route('/api/create_reply/<id>', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def create_reply(id):
    cursor.execute("INSERT INTO thread_reply VALUES (DEFAULT, %s, %s, DEFAULT, %s)",
                   (request.get_json()['author_id'], request.get_json()['content'], id))

    conn.commit()

    return jsonify(status=200)


# END FORUM FUNCTIONALITY

if __name__ == '__main__':
    app.run(host='0.0.0.0')
