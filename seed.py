from socket import ALG_SET_AEAD_ASSOCLEN
from models import User, Post, db
from app import app

db.session.rollback()

# Create all tables
db.drop_all()
db.create_all()

# Id tables isn't empty, empty it
User.query.delete()
Post.query.delete()

# Add users
gary = User(first_name = "Gary", last_name = "Mendez")
elliot = User(first_name = "Elliot", last_name = "Stabler")
michael = User(first_name = "Michael", last_name = "Westen")

# Add new objects to session, so they'll persist
db.session.add(gary)
db.session.add(elliot)
db.session.add(michael)

# Commit otherwise, this'll never get saved
db.session.commit()

first_post=Post(title = "1st Post",
content = "This is the first post!",
user_code = 1
)

db.session.add(first_post)
db.session.commit()
