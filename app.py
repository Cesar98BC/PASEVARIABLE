from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    nombre= "Cesar Briones"
    return render_template('index.html', nombre=nombre)