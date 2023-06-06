from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
import re
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from werkzeug.exceptions import HTTPException, NotFound
import uuid as uuid
from flask import flash
from flask import render_template, redirect, session, request

UPLOAD_FOLDER = 'flask_app/static/img' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 30*1024*1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','mp4'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
        


@app.route('/createPost', methods = ['POST'])
def createPost():
    if request.method == 'POST':
    
        data = {
            'title': request.form['title'],
            'content': request.form['content'],
            'subtitle': request.form['subtitle'],
            'user_id': session['user_id'],
            'categories': request.form['categories']       
        }
    Post.save(data)
    return redirect('/foreditor/createnews')

@app.route('/foreditor/media/delete/<int:id>')
def deletePost(id):
    data = {
        'post_id': id,
        'user_id': session['user_id']
    }
    post = Post.get_post_by_id(data)
    if session['user_id'] == post['user_id']:
        Post.delete(data)
        return redirect('/foreditor/Dashboard')
    return redirect('/foreditor/Dashboard')

@app.route('/editpost/<int:id>/update_post', methods = ['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'user_id': session['user_id'],
        'categories': request.form['categories'],
        'title': request.form['title'],
        'content': request.form['content'],
        'subtitle': request.form['subtitle'],
        'post_id': id
    }
    post = Post.get_post_by_id(data)
    if data['categories'] == '':
        data['categories']=post['categories']
    if data['title'] == '':
        data['title']=post['title']
    if data['content'] == '':
        data['content']=post['content']
    if data['subtitle'] == '':
        data['subtitle']=post['subtitle']

    Post.update(data)
    return redirect('/foreditor/Dashboard')


@app.route('/foreditor/media/updatemedia/<int:id>', methods = ['POST'])
def upload_pic(id):
    if 'user_id' in session:
        file = request.files['filename']
        if file and allowed_file(file.filename):
            pic_filename = secure_filename(file.filename)
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            data = {
                'image': pic_name,
                'user_id': session['user_id'],
                'id' : id
            }
            Post.add_post_image(data)
            return redirect(request.referrer)
        else:
            flash('*This image is not in the right format', 'content')
            return redirect(request.referrer)
    return redirect('/logout')

@app.route('/foreditor/media/updatevideo/<int:id>', methods = ['POST'])
def upload_video(id):
    if 'user_id' in session:
        file = request.files['filename']
        if file and allowed_file(file.filename):
            video_filename = secure_filename(file.filename)
            video_name = str(uuid.uuid1()) + "_" + video_filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], video_name))
            data = {
                'video': video_name,
                'user_id': session['user_id'],
                'id' : id
            }
            Post.add_post_video(data)
            return redirect(request.referrer)
        else:
            flash('*This video is not in the right format', 'content')
            return redirect(request.referrer)
    return redirect('/logout')


@app.route('/foreditor/media/updateinsta/<int:id>', methods = ['POST'])
def updateinsta(id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'user_id': session['user_id'],
        'instaembed': request.form['instaembed'],
        'post_id': id
    }
    post=Post.add_post_instaembed(data)
    if data['instaembed'] == '':
        data['instaembed']=post['instaembed']
    return redirect('/foreditor/Dashboard')

@app.route('/foreditor/media/updateyturl/<int:id>', methods = ['POST'])
def updateyturl(id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'user_id': session['user_id'],
        'yturl': request.form['yturl'],
        'post_id': id
    }
    post=Post.add_post_instaembed(data)
    if data['yturl'] == '':
        data['yturl']=post['yturl']
    return redirect('/foreditor/Dashboard')

@app.route('/foreditor/media/updatefburl/<int:id>', methods = ['POST'])
def updatefburl(id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'user_id': session['user_id'],
        'fburl': request.form['fburl'],
        'post_id': id
    }
    post=Post.add_post_instaembed(data)
    if data['fburl'] == '':
        data['fburl']=post['fburl']
    return redirect('/foreditor/Dashboard')


@app.route('/foreditor/media/updatetturl/<int:id>', methods = ['POST'])
def updatetturl(id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'user_id': session['user_id'],
        'tturl': request.form['tturl'],
        'post_id': id
    }
    post=Post.add_post_instaembed(data)
    if data['tturl'] == '':
        data['tturl']=post['tturl']
    return redirect('/foreditor/Dashboard')

#=================================================================================================================#
#======================================= For Pages used by users =================================================#
#=================================================================================================================#