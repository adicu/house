
from flask import Flask, make_response

app = Flask(__name__)
app.debug = True


@app.route('/be_quiet', methods=['POST'])
def send_groupme():
    pass


@app.route('/')
def main():
    return make_response(open('static/base.html').read())


if __name__ == '__main__':
    app.run()

