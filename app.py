
from flask import Flask, make_response, request
from os import environ
import datetime as DT
import simplejson as JSON
import requests

app = Flask(__name__)
app.debug = True
GROUPME_TOKEN = environ.get('GROUPME_TOKEN')
GROUPME_BOT_ID = environ.get('GROUPME_BOT_ID')

app.LAST_TEXT = None
TIMEOUT_MINUTES = 30


@app.route('/be_quiet', methods=['POST'])
def send_groupme():

    data = JSON.loads(request.data)

    now = DT.datetime.today()
    if app.LAST_TEXT:
        diff = now - app.LAST_TEXT
        if diff.seconds/60 < TIMEOUT_MINUTES:
            return JSON.dumps({
                'message':'Sorry, someone else has used this in the past half hour'
            }), 403


    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id' : GROUPME_BOT_ID,
        'text' : 'Quiet Bot: ' + data['message'],
        'token' : GROUPME_TOKEN
    }
    headers = {
        'Content-Type' : 'Application/json'
    }
    requests.post(url, data=(JSON.dumps(payload)), headers=headers)

    app.LAST_TEXT = DT.datetime.today()
    return JSON.dumps({'message': 'GroupMe texted: "'+data['message']+'"'}), 200


@app.route('/')
def main():
    return make_response(open('static/base.html').read())


if __name__ == '__main__':
    app.run()
