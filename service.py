from flask import Flask, render_template, request
import operations
import json
from bson.json_util import dumps
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/index')
def index():
    user = {'username': 'Zhenjie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/newword', methods=['POST'])
def new_word():
    req_data = request.get_json()
    word = req_data['word']
    mean = req_data['mean']
    note = req_data['note']
    word_uploaded = {
        'word':word,
        'mean':mean,
        'note':note
    }
    return operations.uploadWord(word_uploaded)

@app.route('/words', methods=['GET'])
def get_words():
    return dumps(operations.fetch_words())


if __name__ == '__main__':
    app.run(debug=True)