import urllib2
import json

from httplib2 import Http
from urllib import urlencode
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/text", methods=['POST', 'GET'])
def text():
    error = None
    if request.method == 'POST':
        return text_analyzed(request.form['url'])
    return render_template('text.html', error=error)

@app.route("/ray")
def ray():
    return render_template('ray.html')

@app.route('/connie', methods=['POST','GET'])
def connie():
   return 'TODO get tracks, send to richard'

def texts():
    URL = "http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=6b961c784967a94fe1829d3d065016f87bf38153&outputMode=json&url=http://boingboing.net/2013/01/12/rip-aaron-swartz.html"
    return theText

if __name__ == '__main__':
    app.run()
