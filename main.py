from flask import Flask, render_template,request
from func import*

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])

def hello():
    if request.method=="POST":
        registeration(username=request.form['username'],age=request.form['age'],
                     address=request.form['address'],course=request.form['course'],
                     duration=request.form['duration'])
    data=read_json()
    return render_template("index.html",stud=data["students"])

if __name__=="__main__":
    app.run(debug=True)
