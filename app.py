
from flask import Flask, make_response, request
from os import environ
import sqlite3
from datetime import datetime as DT
import simplejson as JSON
import requests

app = Flask(__name__)
app.debug = True
GROUPME_TOKEN = environ.get('GROUPME_TOKEN')
GROUPME_BOT_ID = environ.get('GROUPME_BOT_ID')

TIMEOUT_MINUTES = 30


def get_conn():
    return sqlite3.connect('log.db')


def get_last_date(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT max(datetime) FROM messages;')
    last = cursor.fetchone()[0]
    if last:
                                #'2013-09-02 20:24:44.244390' 
        return DT.strptime(last, "%Y-%m-%d %H:%M:%S")
    return None


def log_message(conn, msg):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages VALUES (null, ?, ?);", (DT.today().strftime("%Y-%m-%d %H:%M:%S"), msg))
    cursor.close()
    conn.commit()


@app.route('/be_quiet', methods=['POST'])
def send_groupme():
    db = get_conn()

    now = DT.today()
    last = get_last_date(db)

    if last:
        diff = now - last
        if diff.seconds/60 < TIMEOUT_MINUTES:
            return JSON.dumps({
                'message':'Sorry, someone else has used this in the past half hour'
            }), 403


    data = JSON.loads(request.data)
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

    log_message(db, data['message'])
    db.close()
    return JSON.dumps({'message': 'GroupMe texted: "'+data['message']+'"'}), 200


@app.route('/')
def main():
    return make_response(open('static/base.html').read())


if __name__ == '__main__':
    db = get_conn()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (message_index INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT, message TEXT);
    """)
    cursor.close()
    db.commit()
    db.close()
    app.run()
