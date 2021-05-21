
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="Tariq Hasan"

@app.route("/")

def counter():
    if "ad" in session:
        session["ad"]+=1
    else:
        session["ad"]=0

    return render_template("index.html")

@app.route("/destroy")
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True) 

