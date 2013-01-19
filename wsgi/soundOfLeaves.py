import urllib2
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "index"
@app.route("/text")
def text():
    return texts()
from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run()

def texts():
    theText = "To Sherlock Holmes she is always THE woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that oone particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a give and a sneer. They were admirable things for the observer -- excellent for drawing the veil from men's motives and actions. But fo the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory."
    return theText
#stuff = urllib.urlopen("http://www.gutenberg.org/cache/epub/1661/pg1661.txt")
#real = stuff.read()
#stuff.close()
req = urllib2.Request("http://locahost:5000/bookone/sherlock.json")
opener = urllib2.build_opener()
free = opener.open(req)
json = json. loads(free.read())
print json
print json['unit']
