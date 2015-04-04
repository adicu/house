from flask import Flask, Response, request
from displays import functions
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_message():
    data = json.loads(request.data)

    text =  data['text']
    name = data['name']

    functions[name](text)

    return Response(status=200)    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
