from flask import Flask, Response, request
from display import functions
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_message():
    data = json.loads(request.data)

    text =  data['text']
    name = data['name']

    try:
        functions[name](text)
    except:
        pass

    return Response(status=200)    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
