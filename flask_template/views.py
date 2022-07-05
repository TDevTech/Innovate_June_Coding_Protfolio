from flask import Flask, render_template, Blueprint, redirect, url_for



my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    # <h1> ...Hello World....!!! </h1>
    return render_template("index.html")


@my_view.route('/tarig')
def tarig():
    return '<h1> ...This is Tarig\'s first Flask app ....!!! </h1>'

@my_view.route('/home')
def home():
    return render_template("home.html") 

@my_view.route('/portfolio')
def portfolio():
    return render_template("portfolio.html") 

@my_view.route('/services')
def services():
    return render_template("services.html") 

@my_view.route('/login')
def login():
    return render_template("login.html") 

@my_view.route('/help')
def help():
    return render_template("help.html") 

@my_view.route('/contact')
def contact():
    return render_template("contact.html") 

@my_view.route('/about')
def about():
    return render_template("about.html") 
#// redirect 
@my_view.route('/homepage')
def home_redirect():
    return redirect(url_for("my_view.home"))