from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>')
def hello_world(username='Alison'):
    return render_template('script.html', name=username)


@app.route('/height')
def my_height():
    return render_template('height.html')