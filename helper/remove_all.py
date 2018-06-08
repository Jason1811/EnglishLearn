import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "common"))

import mongodb_client

db = mongodb_client.get_db()
db.words.delete_many({})
print('Delete successfully!')