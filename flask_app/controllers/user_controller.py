from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User



@app.route('/')
@app.route("/users")
def index():
    # users = User.get_all()
    # return render_template("index.html", users=users)
    return render_template("users.html", users=User.get_all())

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)
    return redirect("/users")

@app.route("/users/display/<int:id>")
def display_user(id):
    data = {"id":id}
    return render_template("display_one_user.html", user=User.show_one(data))

@app.route("/users/edit/<int:id>")
def edit_user(id):
    data = {"id":id}
    return render_template("edit_user.html", user=User.show_one(data))

@app.route("/users/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/users/remove/<int:id>")
def remove(id):
    data = {"id":id}
    User.delete(data)
    return redirect('/users')