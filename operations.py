import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./", "common"))

import mongodb_client

TABLE_NAME = 'words'

def uploadWord(word):
    db = mongodb_client.get_db()
    list = db.words
   
    result = list.insert_one(word)
    print('One post: {0}'.format(result.inserted_id))
    return 'success!'

def fetch_words():
    db = mongodb_client.get_db()
    list = db.words
    return list.find({})
