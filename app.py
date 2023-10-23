from flask import Flask
from flask_cors import CORS
from flask import render_template

app = Flask(__name__, template_folder='.')
CORS(app)

@app.route('/')
def game():
    return render_template('index.html')