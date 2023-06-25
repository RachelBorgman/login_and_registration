from flask import Flask, render_template, request, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route("/")
def login_page():
    return render_template("login.html")

from flask_app.models.user import User
@app.route('/register/user', methods=["POST"])
def register():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "username": request.form["username"],
        "password": pw_hash,
        "email": request.form["email"]
    }
    new_user_id=User.save(data)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['username'] = request.form['username']
    session['email'] = request.form['email']
    return redirect('/reg_success')

@app.route("/reg_success")
def reg_success():
    return render_template("reg_success.html")

@app.route('/login/user', methods=["POST"])
def login_user():
    if not User.validate_login(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id=User.save(data)
    session['username'] = request.form['username']
    session['email'] = request.form['email']
    return redirect('/login_success')

@app.route("/login_success")
def login_success():
    if 'username' in session:
        return render_template("login_success.html")
    else:
        # flash('Login Not Logged In')
        redirect('/')

@app.route("/logout")
def logout():
    session.clear()
    print("session cleared")
    return render_template("login.html")

# from flask_app.models.user import User
# @app.route('/user_logged_in', methods=["POST"])
# def user_logged_in():
#     data = {
#         "username": request.form["username"],
#         "password": request.form["password"],
#         "email": request.form["email"]
#     }
#     User.save(data)
#     return redirect('/')


# from flask_app.models.user import User
# @app.route("/read_one/<int:id>")
# def read_one(id):
#     data = {
#         'id': id
#     }
#     return render_template("read_one.html", user = User.get_one(data))
    # return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# @app.route('/edit/<int:id>')
# def edit(id):
#     data = {
#         'id': id,
#     }
#     # User.save(data)
#     return render_template("update.html", user = User.get_one(data))

# @app.route('/update', methods=['POST'])
# def update():
#     User.update(request.form)
#     new_user_id = request.form["id"]
#     return redirect(f'/read_one/{new_user_id}')

# @app.route('/delete/<int:id>')
# def delete(id):
#     data = {
#         'id': id
#     }
#     User.delete(data)
#     return redirect('/')