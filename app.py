
from flask import Flask, make_response
from os import environ
import simplejson as JSON
import requests

app = Flask(__name__)
app.debug = True
GROUPME_TOKEN = environ.get('GROUPME_TOKEN')
GROUPME_BOT_ID = environ.get('GROUPME_BOT_ID')


@app.route('/be_quiet', methods=['POST'])
def send_groupme():
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id' : GROUPME_BOT_ID,
        'text' : 'go the sleep',
        'token' : GROUPME_TOKEN
    }
    headers = {
        'Content-Type' : 'Application/json'
    }

    resp = requests.post(url, data=(JSON.dumps(payload)), headers=headers)
    print resp


@app.route('/')
def main():
    return make_response(open('static/base.html').read())


if __name__ == '__main__':
    app.run()
