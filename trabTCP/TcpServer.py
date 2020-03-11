import socket
from flask import Flask
from flask import render_template
import subprocess
import telnetlib

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

host = "127.0.0.1"
port = 100

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = """\
GET /auth HTTP/1.1\r
User-Agent : {user_agent}\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""

app = Flask(__name__)

@app.route('/')
def index():
    # return headers + "\r" + render_template('center.html', return_data='Hello TCP')  
    return "HELLO TCP"

@app.errorhandler(403)
def forbidden():
    return render_template('center.html', return_data='Can\'t do that!' )

@app.errorhandler(404)
def page_not_found():
    return render_template('center.html', return_data='Nothing found here!')

@app.errorhandler(500)
def internal_server():
    return render_template('center.html', return_data='Something smells strange!')

if __name__ == '__main__':
    app.run(host,port)