from flask import Flask, request
import requests

app = Flask(__name__)

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