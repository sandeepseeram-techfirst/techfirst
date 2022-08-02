from flask import Flask
app = Flask(__name__)

"""
Web server routes look up URIs to
determine actions in a way similar to how routing on a network 
performs a best path match to define traffic destinations

"""

@app.route('/newAPI')
def new_api():
    return 'Hello from within your new API'

@app.route('/')
def index():
    return 'Response from Root URL' 

@app.route('/newAPI', methods=['POST'])
def new_api():
if request.method == 'POST':
    args = request.args.get('car')
    body = request.data
    header = request.headers
    cookies = request.cookies
    return 'Hello from within your new API'