import sys
from flask import Flask, render_template, request
from pyechonest import config
from pyechonest import song
config.ECHO_NEST_API_KEY="IY520EPU4LRFUIY8R"
app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/ray")
def ray():
    return render_template('ray.html')

@app.route('/connie', methods=['POST','GET'])
def connie():
    songlist = song.search(mood=search, buckets=['id:spotify-WW', 'tracks'], limit=True, results=5)
    foreign_ids = []
    for item in songlist:
        for t in item.get_tracks('spotify-WW'):
            foreign_ids.append(t['foreign_id'][17:])
        comma = ","
        foreign_id_string = comma.join(foreign_ids)
    return flask.render_template("spotify.html", tracks=foreign_id_string)

@app.route('/john')
def john():
    return 'PARSE TEXT and send results to connie'

@app.route('/playlist', methods=['POST'])
def playlist(tracks=None):
    return render_template('spotify.html', tracks=request.form['tracks'])

if __name__ == '__main__':
    app.run()
