from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post
from flask import render_template, redirect, session, request ,abort,url_for

#=================================================================================================================#
#======================================= For Pages used by users =================================================#
#=================================================================================================================#

@app.route('/foreditor/Dashboard')
def index():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'categories': '2'
        }
        user = User.get_user_by_id(data)
        allposts = Post.get_all()
        post_count = Post.count_posts()
        category_counts = Post.count_posts_by_category()
        category_names = {
            1: 'Aktualitet',
            2: 'Fundit',
            3: 'Rajoni',
            4: 'Bota',            
            5: 'Kultura',
            6: 'Horoskopi',
            7: 'Showbizz',
            8: 'Sport',            
            9: 'Ekonomi',
            10: 'Intervista',
            11: 'Politik',
            12: 'Njoftime',            
            13: 'Guzhine',
            14: 'Fashion',
            15: 'Blog',
            16: 'Opinion',            
        }
        
    return render_template('foreditor/Dashboard.html', users= user,
                                                    allposts= allposts,
                                                    post_count=post_count ,
                                                    category_counts=category_counts, 
                                                    category_names=category_names)

@app.route('/foreditor/enterondashboard')
def enterondashboard():
    if 'user_id' in session:
        return redirect(request.referrer)
    return render_template('foreditor/enterondashboard.html')

@app.route('/login')
def loginPage(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }
    users = User.get_all(data)
    return render_template('foreditor/Dashboard.html',users=users)

@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    if not User.get_user_by_email(data):
        return redirect(request.referrer)
    
    user = User.get_user_by_email(data)

    session['user_id'] = user['id']
    return redirect('/foreditor/Dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/foreditor/enterondashboard')

#=================================================================================================================#
#======================================= For Pages posts by users =================================================#
#=================================================================================================================#

@app.route('/foreditor/createnews')
def createnewspage():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }
        user = User.get_user_by_id(data)
    return render_template('foreditor/createnews.html', users= user)

@app.route('/foreditor/editpost/<int:id>')
def editpostpage(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        user = User.get_user_by_id(data)
        post = Post.get_post_by_id(data)
    return render_template('foreditor/editpostpage.html', users= user,posts = post)

@app.route('/foreditor/detailspage/<int:id>')
def detailspage(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        user = User.get_user_by_id(data)
        post = Post.get_post_by_id(data)
        allposts = Post.get_all()
    return render_template('foreditor/detailspage.html', users= user,posts = post,allposts=allposts)

@app.route('/foreditor/media/updatemedia/<int:id>')
def updateimagepost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        user = User.get_user_by_id(data)
        post = Post.get_post_by_id(data)
    return render_template('foreditor/media/updatemedia.html', users= user,posts = post)


@app.route('/createUser', methods = ['POST'])
def createUser():
    data = {
        'position': request.form['position'],
        'username': request.form['username'],
        'password': request.form['password'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/foreditor/admin/adminstration')
#=================================================================================================================#
#======================================= For Pages used by users =================================================#
#=================================================================================================================#

@app.route('/')
def homepage():
    data = {
        'categories': '2'
    }  # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/homepage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/ShowBiz')
def showbiz():
    data = {
        'categories': '7'
    }  # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/mediaroze.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)


@app.route('/Bota')
def bota():
    data = {'categories': '4'}  # Specify the desired category
    # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/botapage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Rajoni')
def rajoni():
    data = {'categories': '3'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/rajoni.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Sport')
def sporti():
    data = {'categories': '8'}  # Specify the desired category
    # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/sportpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Kultura')
def kultura():
    data = {'categories': '5'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/kulturepage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Fundit')
def fundit():
    data = {'categories': '2'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/funditpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Aktualitet')
def Aktualitet():
    data = {'categories': '1'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/Aktualitetpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Horoskopi')
def horoskopi():
    data = {'categories': '6'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/horoskopipage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Blog')
def blog():
    data = {'categories': '15'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/blogpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Ekonomi')
def ekonomi():
    data = {'categories': '9'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/ekonomipage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Fashion')
def fashion():
    data = {'categories': '14'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/fashionpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Guzhine')
def guzhine():
    data = {'categories': '13'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/guzhinepage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Intervista')
def intervista():
    data = {'categories': '10'}  # Specify the desired category
    # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/intervistapage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)
@app.route('/Njoftime')
def njoftime():
    data = {'categories': '12'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/njoftimepage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Opinion')
def opinion():
    data = {'categories': '16'}  # Specify the desired category
    # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/opinionpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)

@app.route('/Politik')
def politik():
    data = {'categories': '11'}  # Specify the desired category
     # Specify the desired category
    categories = Post.get_last_10_posts(data)
    lastnews = Post.get_last_1_posts(data)
    secondposts = Post.get_second_posts(data)
    thirds = Post.get_third_posts(data)
    fourths = Post.get_forth_posts(data)
    different_category = '1'
    different_category2 = '2'
    different_category3 = '3'
    different_category4 = '4'
    different_category5 = '5'
    different_category6 = '6'
    different_category7 = '7'
    different_category8 = '8'
    different_category9 = '9'
    different_category10 = '10'
    different_category11 = '11'
    different_category12 = '12'
    different_category13 = '13'
    different_category14 = '14'
    different_category15 = '15'
    different_category16 = '16'
    # Specify the different category you want to display
    last4news = Post.get_last_4_posts(different_category)
    lasts1news = Post.get_last_posts(different_category)
    
    last42news = Post.get_last_4_posts(different_category2)
    lasts2news = Post.get_last_posts(different_category2)
    
    last43news = Post.get_last_4_posts(different_category3)
    lasts3news = Post.get_last_posts(different_category3)
    
    last44news = Post.get_last_4_posts(different_category4)
    lasts4news = Post.get_last_posts(different_category4)
    
    last45news = Post.get_last_4_posts(different_category5)
    lasts5news = Post.get_last_posts(different_category5)
    
    last46news = Post.get_last_4_posts(different_category6)
    lasts6news = Post.get_last_posts(different_category6)
    
    last47news = Post.get_last_4_posts(different_category7)
    lasts7news = Post.get_last_posts(different_category7)
    
    last48news = Post.get_last_4_posts(different_category8)
    lasts8news = Post.get_last_posts(different_category8)
    
    last49news = Post.get_last_4_posts(different_category9)
    lasts9news = Post.get_last_posts(different_category9)
    
    last410news = Post.get_last_4_posts(different_category10)
    lasts10news = Post.get_last_posts(different_category10)
    
    last411news = Post.get_last_4_posts(different_category11)
    lasts11news = Post.get_last_posts(different_category11)
    
    last412news = Post.get_last_4_posts(different_category12)
    lasts12news = Post.get_last_posts(different_category12)
    
    last413news = Post.get_last_4_posts(different_category13)
    lasts13news = Post.get_last_posts(different_category13)
    
    last414news = Post.get_last_4_posts(different_category14)
    lasts14news = Post.get_last_posts(different_category14)
    
    last415news = Post.get_last_4_posts(different_category15)
    lasts15news = Post.get_last_posts(different_category15)
    
    last416news = Post.get_last_4_posts(different_category16)
    lasts16news = Post.get_last_posts(different_category16)
    
    allposts = Post.get_post(data)
    return render_template('menu/politikpage.html', categories=categories,
                                                lastnews=lastnews,
                                                secondposts=secondposts,
                                                thirds=thirds,
                                                fourths=fourths,
                                                
                                                last4news=last4news,
                                                lasts1news=lasts1news,
                                                
                                                last42news=last42news,
                                                lasts2news=lasts2news,
                                                
                                                last43news=last43news,
                                                lasts3news=lasts3news,
                                                
                                                last44news=last44news,
                                                lasts4news=lasts4news,
                                                
                                                last45news=last45news,
                                                lasts5ews=lasts5news,
                                                
                                                last46news=last46news,
                                                lasts6news=lasts6news,
                                                
                                                last47news=last47news,
                                                lasts7news=lasts7news,
                                                
                                                last48news=last48news,
                                                lasts8news=lasts8news,
                                                
                                                last49news=last49news,
                                                lasts9news=lasts9news,
                                                
                                                last410news=last410news,
                                                lasts10news=lasts10news,
                                                
                                                last411news=last411news,
                                                lasts11news=lasts11news,
                                                
                                                last412news=last412news,
                                                lasts12news=lasts12news,
                                                
                                                last413news=last413news,
                                                lasts13news=lasts13news,
                                                
                                                last414news=last414news,
                                                lasts14news=lasts14news,
                                                
                                                last415news=last415news,
                                                lasts15news=lasts15news,
                                                
                                                last416news=last416news,
                                                lasts16news=lasts16news,
                                                
                                                allposts=allposts)
#=================================================================================================================#
#======================================= For Pages used for test =================================================#
#=================================================================================================================#
@app.route('/forpost/readpost/<int:id>')
def readpost(id):
        data = {
            'post_id': id,
            'categories': '2'
        }  # Specify the desired category
        post = Post.get_post_by_id(data)
        categories = Post.get_last_10_posts(data)
        lastnews = Post.get_last_1_posts(data)
        secondposts = Post.get_second_posts(data)
        thirds = Post.get_third_posts(data)
        fourths = Post.get_forth_posts(data)
        category_counts = Post.count_posts_by_category()
        
        different_category = '1'
        different_category2 = '2'
        different_category3 = '3'
        different_category4 = '4'
        different_category5 = '5'
        different_category6 = '6'
        different_category7 = '7'
        different_category8 = '8'
        different_category9 = '9'
        different_category10 = '10'
        different_category11 = '11'
        different_category12 = '12'
        different_category13 = '13'
        different_category14 = '14'
        different_category15 = '15'
        different_category16 = '16'
        
        category_names = {
            1: 'Aktualitet',
            2: 'Fundit',
            3: 'Rajoni',
            4: 'Bota',            
            5: 'Kultura',
            6: 'Horoskopi',
            7: 'ShowBiz',
            8: 'Sport',            
            9: 'Ekonomi',
            10: 'Intervista',
            11: 'Politik',
            12: 'Njoftime',            
            13: 'Guzhine',
            14: 'Fashion',
            15: 'Blog',
            16: 'Opinion',            
        }
        
        # Specify the different category you want to display
        last4news = Post.get_last_4_posts(different_category)
        lasts1news = Post.get_last_posts(different_category)
        
        last42news = Post.get_last_4_posts(different_category2)
        lasts2news = Post.get_last_posts(different_category2)
        
        last43news = Post.get_last_4_posts(different_category3)
        lasts3news = Post.get_last_posts(different_category3)
        
        last44news = Post.get_last_4_posts(different_category4)
        lasts4news = Post.get_last_posts(different_category4)
        
        last45news = Post.get_last_4_posts(different_category5)
        lasts5news = Post.get_last_posts(different_category5)
        
        last46news = Post.get_last_4_posts(different_category6)
        lasts6news = Post.get_last_posts(different_category6)
        
        last47news = Post.get_last_4_posts(different_category7)
        lasts7news = Post.get_last_posts(different_category7)
        
        last48news = Post.get_last_4_posts(different_category8)
        lasts8news = Post.get_last_posts(different_category8)
        
        last49news = Post.get_last_4_posts(different_category9)
        lasts9news = Post.get_last_posts(different_category9)
        
        last410news = Post.get_last_4_posts(different_category10)
        lasts10news = Post.get_last_posts(different_category10)
        
        last411news = Post.get_last_4_posts(different_category11)
        lasts11news = Post.get_last_posts(different_category11)
        
        last412news = Post.get_last_4_posts(different_category12)
        lasts12news = Post.get_last_posts(different_category12)
        
        last413news = Post.get_last_4_posts(different_category13)
        lasts13news = Post.get_last_posts(different_category13)
        
        last414news = Post.get_last_4_posts(different_category14)
        lasts14news = Post.get_last_posts(different_category14)
        
        last415news = Post.get_last_4_posts(different_category15)
        lasts15news = Post.get_last_posts(different_category15)
        
        last416news = Post.get_last_4_posts(different_category16)
        lasts16news = Post.get_last_posts(different_category16)
        
        allposts = Post.get_post(data)
        
        return render_template('forposts/readpost.html', categories=categories,
                                                            category_names=category_names,
                                                            post=post,
                                                            lastnews=lastnews,
                                                            category_counts=category_counts, 
                                                            secondposts=secondposts,
                                                            thirds=thirds,
                                                            fourths=fourths,
                                                            
                                                            last4news=last4news,
                                                            lasts1news=lasts1news,
                                                            
                                                            last42news=last42news,
                                                            lasts2news=lasts2news,
                                                            
                                                            last43news=last43news,
                                                            lasts3news=lasts3news,
                                                            
                                                            last44news=last44news,
                                                            lasts4news=lasts4news,
                                                            
                                                            last45news=last45news,
                                                            lasts5ews=lasts5news,
                                                            
                                                            last46news=last46news,
                                                            lasts6news=lasts6news,
                                                            
                                                            last47news=last47news,
                                                            lasts7news=lasts7news,
                                                            
                                                            last48news=last48news,
                                                            lasts8news=lasts8news,
                                                            
                                                            last49news=last49news,
                                                            lasts9news=lasts9news,
                                                            
                                                            last410news=last410news,
                                                            lasts10news=lasts10news,
                                                            
                                                            last411news=last411news,
                                                            lasts11news=lasts11news,
                                                            
                                                            last412news=last412news,
                                                            lasts12news=lasts12news,
                                                            
                                                            last413news=last413news,
                                                            lasts13news=lasts13news,
                                                            
                                                            last414news=last414news,
                                                            lasts14news=lasts14news,
                                                            
                                                            last415news=last415news,
                                                            lasts15news=lasts15news,
                                                            
                                                            last416news=last416news,
                                                            lasts16news=lasts16news,
                                                            
                                                            allposts=allposts)



#=================================================================================================================#
#======================================= For Pages used for test =================================================#
#=================================================================================================================#
@app.route('/tester')
def test():
    return render_template('control/tester/test.html')