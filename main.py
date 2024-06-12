from flask import Flask, render_template,request
from func import*

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def hello():
    msg=""
    if request.method=="POST":
        registeration(username=request.form['username'],age=request.form['age'],
                     address=request.form['address'],course=request.form['course'],
                     duration=request.form['duration'])
        msg=request.form['username']
    data=read_json()
    
    return render_template("index.html",stud=data["students"],msg=msg)

@app.route("/delete/<id>",methods=["POST","GET"])
def delete(id):
    remove(id)
    data=read_json()
    return render_template("index.html",stud=data["students"])

if __name__=="__main__":
    app.run(debug=True)
