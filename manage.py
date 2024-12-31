from app import create_app
from app import engine
from markupsafe import escape
from app.models import Base

# Create all tables
Base.metadata.create_all(bind=engine)
app = create_app()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello1():
    return 'Hello, World'

@app.route("/<name>")
def helloname(name):
    print(name)
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__=="__main__":
    app.run(debug=True)
    