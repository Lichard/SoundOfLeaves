from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/ray")
def ray():
    return render_template('ray.html')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
@app.route('/connie', methods=['POST','GET'])
def connie():
   return 'TODO' 
@app.route('/john')
def john():
    return 'PARSE TEXT'
@app.route('/playlist', methods=['POST'])
def playlist(tracks=None):
    return render_template('spotify.html', tracks=request.form['tracks'])

if __name__ == '__main__':
    app.run()
