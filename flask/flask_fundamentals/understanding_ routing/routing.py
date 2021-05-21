from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello World"

@app.route("/dojo")

def hello_dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_hi(name):
    return "Hi "+name

@app.route("/repeat/<num>/<word>")
def repeat(num,word):
    return (word * int(num))

if __name__=="__main__":
    app.run(debug=True)