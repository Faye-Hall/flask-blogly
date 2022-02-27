"""Blogly application."""

from email.policy import default
from flask import Flask, request, render_template, redirect, flash, session
from sqlalchemy import false
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Homepage"""
    return render_template('home.html')

@app.route('/users_list')
def list_users():
    """Displays list of all users"""
    users = User.query.order_by(User.id.asc()).all()
    return render_template('users_list.html', users=users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    """Displays the new user form"""
    return render_template('new_user_form.html')

@app.route('/users/new', methods=['POST'])
def new_user_form_submit():
    """Handle form submission for creating a new user"""
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'])

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users_list')

@app.route('/users/<user_id>')
def user_id_page(user_id):
    """Displays the invidual user's details"""
    user = User.query.get_or_404(user_id)
    return render_template('detail_page.html',user=user,user_id=user_id)

@app.route('/users/<user_id>/edit', methods=['GET'])
def edit_user_page(user_id):
    """Handles the indviual user's edit form"""
    user = User.query.get(user_id)
    return render_template('user_edit.html',user=user)

@app.route('/users/<user_id>/edit', methods=['POST'])
def edit_user_submit(user_id):
    """Handles indviual user's edit form"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users_list',)


@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user_page(user_id):
    """Delete Selected User"""
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users_list')
