import pprint
import urllib
import json
import sys

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
def connie(URL=None):
    mood = texts(request.form['URL'])
    songlist = song.search(mood, buckets=['tracks','id:spotify-WW'], limit=True, results=5)
    foreign_ids = []
    for item in songlist:
        for t in item.get_tracks('spotify-WW'):
            foreign_ids.append(t['foreign_id'][17:])
        comma = ","
        foreign_id_string = comma.join(foreign_ids)
    print foreign_id_string
    return render_template("spotify.html", tracks=foreign_id_string)

def texts(name):
    analyzeURL = "http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=6b961c784967a94fe1829d3d065016f87bf38153&outputMode=json&url=" + name
    jsonResponse=json.loads(urllib.urlopen(analyzeURL).read())
    #do a check for status ok.
    #then go into the dictionary for the docSentiment and pull out the type.
    pprint.pprint(jsonResponse)
    docSentiment = jsonResponse[u'docSentiment']
    mood = docSentiment[u'type']
    print mood
    return mood

if __name__ == '__main__':
    app.run()
