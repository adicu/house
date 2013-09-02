
from flask import Flask, make_response, request
from os import environ
import datetime as DT
import simplejson as JSON
import requests

app = Flask(__name__)
app.debug = True
GROUPME_TOKEN = environ.get('GROUPME_TOKEN')
GROUPME_BOT_ID = environ.get('GROUPME_BOT_ID')

TIMEOUT_MINUTES = 30


@app.route('/be_quiet', methods=['POST'])
def send_groupme():
    last_text = DT.datetime.strptime(request.cookies.get('last_text'))
    now = DT.datetime.today()

    diff =  now - last_text
    if diff.seconds/60 < TIMEOUT_MINUTES:
        return 'Sorry, you must wait {} minutes before sending another text', 403


    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'bot_id' : GROUPME_BOT_ID,
        'text' : 'go the sleep',
        'token' : GROUPME_TOKEN
    }
    headers = {
        'Content-Type' : 'Application/json'
    }
    #resp = requests.post(url, data=(JSON.dumps(payload)), headers=headers)
    print url, payload, headers


    #if resp.status_code == 201:
    if True:
        response = make_response()
        response.set_cookie('last_text', DT.datetime.today().utcnow())
        return response
    else:
        return 'Error posting message to GroupMe', 501

@app.route('/')
def main():
    return make_response(open('static/base.html').read())


if __name__ == '__main__':
    app.run()
