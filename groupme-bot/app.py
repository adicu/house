from flask import Flask, request
import requests

app = Flask(__name__)

def handshake():
    data = {
        'channel':'/meta/handshake',
        'version':'1.0',
        'supportedConnectionTypes':['long-polling'],
        'id':'1'
    }
    r = requests.post('https://push.groupme.com/faye', data=data)

    if r.status_code == requests.codes.ok:
        return r.content

@app.route('/', methods=['POST'])
def handle_message():
    text = request.form['text']
    sender = request.form['sender']

    display_message(sender, text)

    pass

def display_message(sender, text):
    pass

if __name__ == '__main__':
    app.run()