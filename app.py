"""Blogly application."""

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
    users = User.query.all()
    return render_template('users_list.html', users=users)

@app.route('/users/new', methods=['GET','POST'])
def new_user_form():
    """Displays the new user form"""
    return render_template('new_user_form.html')

@app.route('/users/<user_id>')
def user_id_page(user_id):
    """Displays the invidual user's details"""
    user = User.query.get(user_id)
    return render_template('detail_page.html',user=user)

@app.route('/users/<user_id>/edit', methods=['GET','POST'])
def edit_user_page(user_id):
    """Displays the indviual user's edit form"""
    user = User.query.get(user_id)
    return render_template('user_edit.html',user=user)

@app.route('/users/<user_id>/delete', methods=['POST'])
def hdelete_user_page():
    """******"""
    return render_template('*.html')
