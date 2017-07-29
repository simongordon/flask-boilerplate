
from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter()
def meme(value):
    return 'meme ' + value + ' meme'
#app.jinja_env.filters['meme'] = meme

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route("/other")
def other():
    my_list=[1,2,3]
    return render_template('other.html', title='Other Page', my_list=my_list)

@app.route("/react")
def react_page():
    return render_template('react.html', title='React Page')
