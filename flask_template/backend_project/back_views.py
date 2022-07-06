
from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")
# // redirect 
@my_view.route('/home')
def home_redirect():
    return redirect(url_for("index.home"))


@my_view.route('/Page1')
def Page1():
    return render_template("Page1.html") 
    # // redirect 
@my_view.route('/1')
def Page1_redirect():
    return redirect(url_for("page1.home"))


@my_view.route('/Page2')
def Page2():
    return render_template("Page2.html")
    # // redirect 
@my_view.route('/2')
def Page2_redirect():
    return redirect(url_for("Page2.home")) 


@my_view.route('/Page3')
def Page3():
    return render_template("Page3.html") 
# // redirect 
@my_view.route('/3')
def Page3_redirect():
    return redirect(url_for("Page3.home"))

@my_view.route('/Page4')
def Page4():
    return render_template("Page4.html") 
# // redirect 
@my_view.route('/4')
def Page3_redirect():
    return redirect(url_for("Page4.home"))

@my_view.route('Page5')
def Page5():
    return render_template("Page5.html") 
# // redirect 
@my_view.route('/5')
def Page3_redirect():
    return redirect(url_for("Page5.home"))

@my_view.route('/admin')
def admin():
    return render_template("admin.html") 
# // redirect 
@my_view.route('/administrator')
def admin_redirect():
    return redirect(url_for("admin.home"))
