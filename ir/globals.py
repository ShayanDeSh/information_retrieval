import os
import ujson

inverted_index = {}

if os.path.isfile('index.js'):
    with open('index.js') as f:
        inverted_index = ujson.loads(f)
else:
    print("No file has been indexed")
