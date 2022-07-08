from flask import Flask, render_template, Blueprint, redirect, url_for, abort

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/home')
def home_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route('/page1')
def page1():
    return render_template("page1.html") 
    # // redirect 
@my_view.route('/1')
def page1_redirect():
    return redirect(url_for("my_view.page1"))

@my_view.route('/page2')
def page2():
    return render_template("page2.html")
    # // redirect 
@my_view.route('/2')
def page2_redirect():
    return redirect(url_for("my_view.page2")) 

@my_view.route('/page3')
def page3():
    return render_template("page3.html") 
# // redirect 
@my_view.route('/3')
def page3_redirect():
    return redirect(url_for("my_view.page3"))

@my_view.route('/page4')
def page4():
    return render_template("page4.html") 
# // redirect 
@my_view.route('/4')
def page4_redirect():
    return redirect(url_for("my_view.page4"))

@my_view.route('/page5')
def page5():
    return render_template("page5.html") 
# // redirect 
@my_view.route('/5')
def page5_redirect():
    return redirect(url_for("my_view.page5"))

@my_view.route('/admin')
def admin():
    return render_template("admin.html") 
# // redirect 
@my_view.route('/administrator')
def admin_redirect():
    return redirect(url_for("my_view.admin"))

@my_view.route('/javascript')
@my_view.route('/js')
@my_view.route('/home')
def indx_redirect():
    return redirect(url_for("my_view.index"))

# @my_view.errorhandler(404)
# def not_found():
    #  return render_template("404.html")