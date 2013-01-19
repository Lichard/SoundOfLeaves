from flask import render_template
app = Flask(__name__)

@app.route("/hello/")
@app.route('/hello/<name>')
def hello():
    return render_template('hello.html', name=name)

@app.route("/")
def hi():
    return "hi"

if __name__ == '__main__':
    app.run()
