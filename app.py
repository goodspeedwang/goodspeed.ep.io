from flask import Flask,send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world!\n'

@app.route('/proxy')
def proxy():
    return "Proxy is here."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)