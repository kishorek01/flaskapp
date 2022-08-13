from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route('/hello')
def hello():
    return 'Hello, Kishore'
if __name__ == '__main__':
    app.run()
