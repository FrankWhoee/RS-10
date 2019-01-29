import json

f = open("RS-10_data.json").read()
data = json.loads(f)

with open("questions", "w+", encoding='utf8') as questions:
    for question in data.keys():
        questions.write(question + "\n")

with open("comments", "w+", encoding='utf8') as comments:
    for comment in data.values():
        comments.write(comment + "\n")
