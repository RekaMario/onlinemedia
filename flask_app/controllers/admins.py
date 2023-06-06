from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
import matplotlib.pyplot as plt
from flask import render_template, redirect, session, request ,abort




@app.route('/foreditor/admin/adminstration')    
def admin_only():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }    
    is_admin = User.check_admin_status(data)
    user = User.get_user_by_id(data)
    allposts = Post.get_all()
    allusers = User.get_all()
    
    if not is_admin:
        abort(403)
    return render_template('foreditor/admin/adminstrationpage.html',is_admin = is_admin ,  users = user,allposts=allposts , allusers=allusers)



@app.route('/foreditor/admin/addnewuser')    
def add_newuser():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }    
    is_admin = User.check_admin_status(data)
    user = User.get_user_by_id(data)
    allposts = Post.get_all()
    allusers = User.get_all()
    
    if not is_admin:
        abort(403)
    return render_template('foreditor/admin/addnewuserpage.html',is_admin = is_admin ,  users = user,allposts=allposts , allusers=allusers)



