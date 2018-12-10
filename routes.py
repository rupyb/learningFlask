from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

from app import app

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/learningflask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

app.secret_key = "developement-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
    #   newuser = User('john', 'smith', 'app@poo.com', 'abcd')

      db.session.add(newuser)
      db.session.commit()
      return 'Success!'

  elif request.method == "GET":
    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)   