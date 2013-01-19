from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/ray")
def ray():
    return render_template('ray.html')

@app.route('/connie', methods=['POST','GET'])
def connie():
   return 'TODO get tracks, send to richard' 

@app.route('/john')
def john():
    return 'PARSE TEXT and send results to connie'

@app.route('/playlist', methods=['POST'])
def playlist(tracks=None):
    return render_template('spotify.html', tracks=request.form['tracks'])

if __name__ == '__main__':
    app.run()
