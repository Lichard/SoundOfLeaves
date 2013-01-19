import urllib2
import json
import sys

from httplib2 import Http
from urllib import urlencode
from flask import Flask, render_template, request
from pyechonest import config
from pyechonest import song
config.ECHO_NEST_API_KEY="IY52OEPU4LRFUIY8R"
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

@app.route('/connie', methods=['POST'])
def connie(mood=None):
    songlist = song.search(mood=request.form['mood'], buckets=['tracks','id:spotify-WW'], limit=True, results=5)
    foreign_ids = []
    for item in songlist:
        for t in item.get_tracks('spotify-WW'):
            foreign_ids.append(t['foreign_id'][17:])
        comma = ","
        foreign_id_string = comma.join(foreign_ids)
    print foreign_id_string
    return render_template("spotify.html", tracks=foreign_id_string)

def texts(name):
    URL = "http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=6b961c784967a94fe1829d3d065016f87bf38153&outputMode=json&url=" + name
    data = json.load(urllib2.urlopen('http://access.alchemyapi.com/calls/html/HTMLGetTextSentiment?apikey=6b961c784967a94fe1829d3d065016f87bf38153&outputMode=json&url=http://www.classicshorts.com/stories/danger.html'))
    #This is where we json parse.
    return name

if __name__ == '__main__':
    app.run()
