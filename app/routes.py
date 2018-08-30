from flask import render_template, flash, redirect, url_for
from app import app, db
#from . import submission
#from app.forms import LoginForm

@app.route("/")
def home():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

@app.route("/blog/<user>")
def blog():
    return render_template('blog.html', title='Home', user=user, posts=posts)

@app.route("/artshow")
def artshow():
    submissions = Submission.query.all()
    return render_template('artshow.html', title='artshow')
                           
@app.route("/submission")
def submission():
    return render_template('submission.html')