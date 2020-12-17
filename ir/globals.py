import os
import ujson

inverted_index = {}

if os.path.isfile('index.json'):
    with open('index.json') as f:
        print('here')
        inverted_index = ujson.loads(f.read())
        print(inverted_index)
else:
    print("No file has been indexed")
