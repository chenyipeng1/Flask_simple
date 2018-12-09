from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/admin")
def admin():
    return render_template("admin.html", entries=model.get_entries())

@app.route("/delete", methods=["POST"])
def deleteentry():
    index = request.form["id"]
    model.delete_entry(index)
    return redirect("/admin")

@app.route("/edit", methods=["POST"])
def editentry():
    index = request.form["id"]
    edit = request.form["edit"]
    model.edit_entry(index, edit)
    return redirect("/admin")


if __name__=="__main__":
    model.init()
    app.run(debug=True)