from flask import render_template, url_for, flash, redirect
from pythonblog import app, db, bcrypt
from pythonblog.forms import RegistrationForm, LoginForm
from pythonblog.models import User, Post



posts = [
    {
        'author': 'Travis Pandos',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Sawako Pandos',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2021'
    },
    {
        'author': 'Chris Morales',
        'title': 'Blog Post 3',
        'content': 'Thanks for your help dude.',
        'date_posted': 'Sept 30, 2021'
    }

]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now go ahead and login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check login credentials', 'danger')
    return render_template('login.html', title='Login', form=form)