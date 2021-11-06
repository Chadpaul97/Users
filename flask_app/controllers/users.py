from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
    }
    User.save_user(data)
    return redirect('/read')


@app.route("/read")
def show_users():
    users = User.get_all()
    print(users)
    return render_template('read.html', users=users)

@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect("/")


@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id
    }
    user = User.get_user_info(data)
    return render_template("edituser.html",user=user)

@app.route("/edituser/<int:id>",methods=["POST"])
def edit_user_db(id):
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.edit_user(data)
    return redirect("/")


@app.route('/showuser/<int:id>')
def showuser(id):
    data = {
        "id":id,
    }
    user = User.get_user_info(data)
    return render_template("showuser.html",user=user)


