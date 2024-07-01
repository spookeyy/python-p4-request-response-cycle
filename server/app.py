#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
    <html>
        <head>
            <title>App: {appname}</title>
        </head>
        <body>
            <h1>The name of this application is {appname}</h1>
            <p>The Host for this page: {host}</p>
            <p>The path for this page: {g.path}</p>
        </body>
    </html>
    '''

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
