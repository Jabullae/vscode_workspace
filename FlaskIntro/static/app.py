# https://markupsafe.palletsprojects.com/en/2.0.x/
from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<username>/')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>/')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)   # http://localhost:5000/path/lookup/<br> 입력으로 escape 함수 효과 확인!


if __name__ == '__main__':
    app.run(debug=True)
