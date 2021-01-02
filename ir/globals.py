import os
import ujson

inverted_index = {}
docs_vec_length = {}

if os.path.isfile('index.json'):
    with open('index.json') as f:
        inverted_index = ujson.loads(f.read())
else:
    print("No file has been indexed")


if os.path.isfile('vec.json'):
    with open('vec.json') as f:
        docs_vec_length = ujson.loads(f.read())
else:
    print("No file has been indexed")
