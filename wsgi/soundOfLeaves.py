import urllib, json, sys
#import json
#import sys #Why is this here? Do we need it?
from flask import Flask, render_template, request
from pyechonest import config, song
#from pyechonest import song

config.ECHO_NEST_API_KEY="IY52OEPU4LRFUIY8R"
ALCHEMY_API_KEY="6b961c784967a94fe1829d3d065016f87bf38153"
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('ray.html')

@app.route("/text", methods=['POST', 'GET'])
def text():
    error = None
    if request.method == 'POST':
        return text_analyzed(request.form['url'])
    return render_template('text.html', error=error)

@app.route('/playlist', methods=['POST'])
def connie(URL=None):
    mood = texts(request.form['URL'])
    songlist = song.search(mood=mood, buckets=['tracks','id:spotify-WW'], limit=True, results=20)
    foreign_ids = []
    for item in songlist:
        for t in item.get_tracks('spotify-WW'):
            foreign_ids.append(t['foreign_id'][17:])
        comma = ","
        foreign_id_string = comma.join(foreign_ids)
    return render_template("playlist.html", tracks=foreign_id_string)

def texts(name):
    global ALCHEMY_API_KEY
    analyzeURL = "http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=" + ALCHEMY_API_KEY + "&outputMode=json&url=" + name
    jsonResponse=json.loads(urllib.urlopen(analyzeURL).read())
    docSentiment = jsonResponse[u'docSentiment']
    mood = docSentiment[u'type']
    if mood == 'positive':
        mood='happy'
    else:
        mood='sad'
    return mood

if __name__ == '__main__':
    app.run()
