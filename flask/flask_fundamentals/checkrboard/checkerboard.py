from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def levle1():
    return render_template('index.html',num_row=8,num_col=8)

@app.route('/<num>')

def levle2(num):
    return render_template('index.html',num_row=int(num), num_col=8)

@app.route('/<num>/<num1>')

def levle3(num,num1):
    return render_template('index.html',num_row=int(num), num_col=int(num1))


if __name__=="__main__":
    app.run(debug=True)