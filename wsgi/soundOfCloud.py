from flask import Flask, reunder_template
app = Flask(__name__)

@app.route("/")
def index():
    return 'Index'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello():
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
