import json
import os

files = os.listdir()

for each in files[:10]:
    with open(each, encoding="utf-8") as text:
        data = json.load(text)['Problem']
        print(data)
