from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/<username>')
def user(username='Alison'):
    return render_template('script.html', name=username)

@app.route('/<username>/<int:post_id>')
def post(username='Alison', post_id=None):
    return render_template('post.html', name=username, id=post_id)


@app.route('/height')
def my_height():
    return render_template('height.html')