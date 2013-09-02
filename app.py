
from flask import Flask, make_response
import simplejson as JSON
import requests

app = Flask(__name__)
app.debug = True


@app.route('/be_quiet', methods=['POST'])
def send_groupme():
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
        'id' : 'XXXXXXXXX',
        'text' : 'go the sleep',
        'token' : 'YYYYYYY'
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
