from flask import Flask, render_template, request, Response, jsonify
import operations
import json
from bson.json_util import dumps
app = Flask(__name__)

@app.route('/')
def index():
    user = {'username': 'Zhenjie'}
    return render_template('index.html', title='Home', user=user)


@app.route('/newword', methods=['POST'])
def new_word():

    req_data = request.form
    word = req_data['word']
    mean = req_data['mean']
    note = req_data['note']
    word_uploaded = {
        'word':word,
        'mean':mean,
        'note':note
    }
    if operations.uploadWord(word_uploaded) == 1:
    #     # return Response("{'a':'b'}", status=201, mimetype='application/json')
        return 'success!'
         
@app.route('/words', methods=['GET'])
def get_words():
    return render_template('word_list.html', words=operations.fetch_words())
    # return dumps(operations.fetch_words())


if __name__ == '__main__':
    app.run(debug=True)
