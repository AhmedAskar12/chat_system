from flask import Blueprint, flash, request, url_for,render_template, redirect,session, app, current_app as app
from flask_login import login_required, login_user,logout_user
from .forms import LoginForm, CreateAccountForm
from core.models import User
from flask_login import login_required, current_user
from core.models import User
from core import db

####changed to authentication_blueprint
auth=Blueprint("authentication_blueprint", __name__, url_prefix="/")

@auth.route("/", methods=["POST","GET"])
def start():

    return redirect("/login")


@auth.route("/login", methods=["POST","GET"])
def login():
    login_form = LoginForm(request.form)
    if request.method == "POST":

        if 'login' in request.form:

            # read form data
            username = request.form['username']
            password = request.form['password']

            # Locate user
            user = User.query.filter_by(username=username).first()

            # Check the password
            if user and user.password==password:

                login_user(user)
             
                return redirect('/agents')


            # Something (user or pass) is not ok
            return render_template('auth/login.html',
                                msg='Wrong user or password',
                                form=login_form)

        if not current_user.is_authenticated:
            return render_template('auth/login.html',
                                form=login_form)
 
    return render_template("auth/login.html", segment='index',form=login_form)

@auth.route("/register", methods=["POST","GET"])
def register():
    create_account_form = CreateAccountForm(request.form)
    if request.method == "POST":
    
        

        if 'register' in request.form:

            # read form data
            username = request.form['username']
            password = request.form['password']

            # Locate user
            user = User.query.filter_by(username=username).first()

            # Check the password
            if user:

                return render_template('auth/register.html',
                                msg='Username already registered',
                                   success=False,
                                form=create_account_form)
            
            
            user = User(username=username, password=password,email="", agent=True)
      

            db.session.add(user)
            db.session.commit()


            return render_template('auth/login.html',
                                msg='Account Created Successfully',
                                success=True,
                                form=create_account_form)

        if not current_user.is_authenticated:
            return render_template('auth/register.html',
                                form=create_account_form)
 
    return render_template("auth/register.html", segment='index',form=create_account_form)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop("id",None)
    flash('You have successfully logged yourself out.')
    return redirect('/login')
