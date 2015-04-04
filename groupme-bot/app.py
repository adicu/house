from flask import Flask, Response, request
from displays import functions
from images import display_text
import json
from sys import argv

app = Flask(__name__)
debug = len(argv) > 1 and argv[1] == 'debug'


@app.route('/', methods=['POST'])
def handle_message():
    data = json.loads(request.data)

    text = data['text']
    name = data['name']

    if name in functions:
        functions[name](text)

    display_text_message(name, text)

    return Response(status=200)


def display_text_message(name, text):
    display_text([
        (name + ": ", (255, 0, 0)),
        (text, (0, 255, 0))
    ])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=debug)
